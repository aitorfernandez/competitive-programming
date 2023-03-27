fn clean_input(s: String) -> String {
    s.to_lowercase()
        .chars()
        .filter(|c| c.is_alphanumeric())
        .collect()
}

fn is_palindrome(s: String) -> bool {
    let input = clean_input(s);
    input.chars().rev().eq(input.chars())
}

fn main() {
    assert!(is_palindrome("A man, a plan, a canal: Panama".to_string()));
    assert!(is_palindrome("".to_string()));

    assert!(!is_palindrome("race a car".to_string()));
}
