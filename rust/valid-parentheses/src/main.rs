fn is_valid(s: String) -> bool {
    let mut v: Vec<char> = Vec::new();

    for c in s.chars() {
        match c {
            '(' | '{' | '[' => {
                v.push(c);
            }
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
            _ => continue,
        }
    }

    v.is_empty()
}

fn main() {
    assert!(is_valid("(sadasda())".to_string()));
    assert!(is_valid("()[]{}".to_string()));

    assert!(!is_valid("(]".to_string()));
    assert!(!is_valid("[[".to_string()));
}
