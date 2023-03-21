fn sort(s: String) -> String {
    let mut chars: Vec<_> = s.chars().collect();
    chars.sort_by(|a, b| a.cmp(b));

    // String::from_iter(chars)
    chars
        .into_iter()
        .map(|c| c.to_string())
        .collect::<Vec<_>>()
        .join("")
}

fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    use std::collections::HashMap;

    if strs.len() == 1 {
        return vec![strs];
    }

    let mut hm: HashMap<String, Vec<String>> = HashMap::new();

    for s in strs {
        let sorted_str = sort(s.to_string());

        hm.entry(sorted_str)
            .and_modify(|v| (*v).push(s.to_string()))
            .or_insert(vec![s]);
    }

    hm.into_values().collect()
}

fn main() {
    let res = group_anagrams(vec![
        "eat".to_string(),
        "tea".to_string(),
        "tan".to_string(),
        "ate".to_string(),
        "nat".to_string(),
        "bat".to_string(),
    ]);

    println!("{res:?}");
}
