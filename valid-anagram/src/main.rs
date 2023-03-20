fn sort(s: String) -> String {
    let mut chars: Vec<_> = s.chars().collect();
    chars.sort_by(|a, b| b.cmp(a));

    String::from_iter(chars)
}

fn is_anagram(s: String, t: String) -> bool {
    // sort(s) == sort(t)

    use std::collections::HashMap;

    let mut hm = HashMap::new();
    s.chars().for_each(|c| *hm.entry(c).or_insert(0) += 1);
    t.chars().for_each(|c| *hm.entry(c).or_insert(0) -= 1);

    hm.into_values().all(|v| v == 0)
}

fn main() {
    assert!(is_anagram("anagram".to_string(), "nagaram".to_string()));

    assert!(!is_anagram("rat".to_string(), "cat".to_string()));
}
