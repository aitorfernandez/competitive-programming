pub fn length_of_longest_substring(s: String) -> i32 {
    // use std::collections::HashSet;

    // let hs: HashSet<_> = s.chars().collect();

    // hs.len() as i32

    s.chars()
        .fold(String::new(), |mut acc, el| {
            if !acc.contains(el) {
                acc.push(el)
            }
            acc
        })
        .len() as i32
}

fn main() {
    assert!(length_of_longest_substring("abcabcbb".to_string()) == 3);
    assert!(length_of_longest_substring("bbb".to_string()) == 1);
}
