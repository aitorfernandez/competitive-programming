use std::collections::HashMap;

fn is_anagram(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut hm: HashMap<char, i32> = HashMap::new();

    for (c1, c2) in s.chars().zip(t.chars()) {
        *hm.entry(c1).or_insert(0) += 1;
        *hm.entry(c2).or_insert(0) -= 1;
    }

    hm.values().all(|v| *v == 0)
}

fn main() {
    assert!(is_anagram("anagram".to_string(), "nagaram".to_string()));
    assert!(!is_anagram("rat".to_string(), "car".to_string()));
}
