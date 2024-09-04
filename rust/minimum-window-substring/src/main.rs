use std::collections::HashMap;

fn min_window(s: String, t: String) -> String {
    if t == String::new() || s.len() < t.len() {
        return String::new();
    }

    let mut count: HashMap<char, i32> = HashMap::new();
    let mut window: HashMap<char, i32> = HashMap::new();

    let (mut minimun, mut range, mut l) = (usize::MAX, (-1 as i32, -1 as i32), 0);

    for c in t.chars() {
        *count.entry(c).or_default() += 1;
    }

    let (mut have, need) = (0, count.len());

    let cc: Vec<char> = s.chars().collect();

    for r in 0..cc.len() {
        let c = cc[r];

        *window.entry(c).or_default() += 1;
        have += (window.get(&c) == count.get(&c)) as usize;

        while have == need {
            if (r - l + 1) < minimun {
                range = (l as i32, r as i32);
            }

            minimun = minimun.min(r - l + 1);

            *window.get_mut(&cc[l]).unwrap() -= 1;

            if window.get(&cc[l]) < count.get(&cc[l]) {
                have -= 1;
            }
            l += 1;
        }
    }

    if range.0 > -1 && range.1 > -1 {
        return cc[range.0 as usize..=range.1 as usize]
            .into_iter()
            .collect();
    }

    String::new()
}

fn main() {
    assert_eq!(
        min_window("ADOBECODEBANC".to_string(), "ABC".to_string()),
        "BANC".to_string()
    );
    assert_eq!(
        min_window("a".to_string(), "a".to_string()),
        "a".to_string()
    );
    assert_eq!(
        min_window("a".to_string(), "aa".to_string()),
        "".to_string()
    );
}
