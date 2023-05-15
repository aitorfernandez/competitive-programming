use std::collections::HashMap;

pub fn character_replacement(s: String, k: i32) -> i32 {
    let cc: Vec<_> = s.chars().collect();
    let (mut res, mut l, mut maxf) = (0, 0, 0);
    let mut count: HashMap<char, u64> = HashMap::new();

    for r in 0..s.len() {
        // count.entry(s[r]).and_modify(|v| *v += 1).or_insert(1);
        *count.entry(cc[r]).or_default() += 1;
        maxf = maxf.max(*count.get(&cc[r]).unwrap());

        while (r - l + 1) - maxf as usize > k as usize {
            *count.get_mut(&cc[l]).unwrap() -= 1;
            l += 1;
        }

        res = res.max(r - l + 1);
    }

    res as i32
}

fn main() {
    assert_eq!(character_replacement("ABAB".to_string(), 2), 4);
    assert_eq!(character_replacement("AABABBA".to_string(), 1), 4);
}
