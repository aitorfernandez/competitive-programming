use std::collections::HashMap;

fn sort(s: String) -> String {
    let mut key: Vec<char> = s.chars().collect();
    key.sort();
    // key.sort_by(|a, b| b.cmp(a));
    key.into_iter().collect()
}

fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut hm: HashMap<String, Vec<String>> = HashMap::new();

    for s in strs {
        let key = sort(s.clone());
        hm.entry(key).or_insert(vec![]).push(s);
    }

    let mut res: Vec<Vec<String>> = hm.into_values().collect();
    for group in &mut res {
        group.sort();
    }

    res
}

fn main() {
    assert_eq!(
        group_anagrams(vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string()
        ]),
        vec![
            vec!["bat".to_string()],
            vec!["nat".to_string(), "tan".to_string()],
            vec!["ate".to_string(), "eat".to_string(), "tea".to_string()]
        ]
    );
}
