fn main() {
    println!("group-anagrams");
}

pub fn group_anagrams(strs: Vec<&str>) -> Vec<Vec<&str>> {
    use std::collections::HashMap;

    let mut hm: HashMap<String, Vec<&str>> = HashMap::new();
    for str in strs {
        let mut chars = str.chars().collect::<Vec<char>>();
        chars.sort_unstable();
        let key = chars.into_iter().collect::<String>();
        hm.entry(key).or_default().push(str);
    }
    hm.into_values().collect()
}

#[test]
fn group_anagrams_test() {
    struct TestData<'a> {
        input: Vec<&'a str>,
        // output: Vec<Vec<&'a str>>,
    }

    for t in vec![
        TestData {
            input: vec!["eat", "tea", "tan", "ate", "nat", "bat"],
            // output: vec![vec!["bat"], vec!["nat", "tan"], vec!["ate", "eat", "tea"]],
        },
        TestData {
            input: vec![""],
            // output: vec![vec![""]],
        },
        TestData {
            input: vec!["a"],
            // output: vec![vec!["a"]],
        },
    ] {
        let res = group_anagrams(t.input.clone());
        for i in res.iter().flatten() {
            assert!(t.input.contains(i));
        }
    }
}
