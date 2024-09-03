use std::collections::HashMap;

pub fn is_anagram(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut hm: HashMap<char, i32> = HashMap::new();

    for (a, b) in s.chars().zip(t.chars()) {
        *hm.entry(a).or_default() += 1;
        *hm.entry(b).or_default() -= 1;
    }

    hm.into_values().all(|v| v == 0)
}

fn main() {
    assert!(is_anagram("anagram".to_string(), "nagaram".to_string()));

    assert!(!is_anagram("rat".to_string(), "car".to_string()));
}
