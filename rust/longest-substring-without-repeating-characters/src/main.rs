use std::collections::VecDeque;

fn length_of_longest_substring(s: String) -> i32 {
    let mut len = 0;
    let mut q: VecDeque<char> = VecDeque::new();

    for c in s.chars() {
        while q.contains(&c) {
            q.pop_front();
        }

        q.push_back(c);

        len = len.max(q.len());
    }

    len as i32
}

fn main() {
    assert_eq!(length_of_longest_substring("abcabcbb".to_string()), 3);
    assert_eq!(length_of_longest_substring("bbbbb".to_string()), 1);
    assert_eq!(length_of_longest_substring("pwwkew".to_string()), 3);
}
