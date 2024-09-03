use std::collections::HashMap;

fn sort(s: String) -> String {
    let mut v: Vec<char> = s.chars().collect();
    v.sort_by(|a, b| b.cmp(&a));

    v.iter().collect()
}

fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut hm: HashMap<String, Vec<String>> = HashMap::new();

    for s in strs {
        let k = sort(s.clone());

        hm.entry(k)
            .and_modify(|v| v.push(s.clone()))
            .or_insert(vec![s.clone()]);
    }

    hm.into_values().collect()
}

fn main() {
    let anagrams = group_anagrams(vec![
        "eat".to_string(),
        "tea".to_string(),
        "tan".to_string(),
        "ate".to_string(),
        "nat".to_string(),
        "bat".to_string(),
    ]);
    println!("{anagrams:?}");
}
