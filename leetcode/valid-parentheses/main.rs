fn is_valid(s: String) -> bool {
    let mut v: Vec<char> = vec![];

    for c in s.chars() {
        match c {
            ')' => {
                if v.pop() != Some('(') {
                    return false;
                }
            }
            '}' => {
                if v.pop() != Some('{') {
                    return false;
                }
            }
            ']' => {
                if v.pop() != Some('[') {
                    return false;
                }
            }
            _ => {
                v.push(c);
            }
        }
    }

    true
}

fn main() {
    assert!(is_valid("()[]{}".to_string()));
    assert!(is_valid("([])".to_string()));

    assert!(!is_valid("(}".to_string()));
}
