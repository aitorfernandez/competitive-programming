use std::collections::HashMap;

fn character_replacement(s: String, k: i32) -> i32 {
    let mut hm: HashMap<char, i32> = HashMap::new();
    let (mut longest, mut l, mut max_hm) = (0, 0, 0);

    let cc: Vec<char> = s.chars().collect();

    for r in 0..cc.len() {
        *hm.entry(cc[r]).or_default() += 1;
        max_hm = max_hm.max(hm[&cc[r]]);

        while (r - l + 1) as i32 - max_hm > k {
            *hm.get_mut(&cc[l]).unwrap() -= 1;
            l += 1;
        }

        longest = longest.max(r - l + 1);
    }

    longest as i32
}

fn main() {
    assert_eq!(character_replacement("ABAB".to_string(), 2), 4);
    assert_eq!(character_replacement("AABABBA".to_string(), 1), 4);
}
