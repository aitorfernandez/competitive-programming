fn clean(s: String) -> String {
    s.to_lowercase()
        .chars()
        .filter(|c| c.is_alphanumeric())
        .collect()
}

fn is_palindrome(s: String) -> bool {
    let cc: Vec<char> = clean(s).chars().collect();
    if cc.is_empty() {
        return true;
    }

    let (mut l, mut r) = (0, cc.len() - 1);

    while r > l {
        if cc[l] != cc[r] {
            return false;
        }
        l += 1;
        r -= 1;
    }

    true
}

fn main() {
    assert!(is_palindrome("A man, a plan, a canal: Panama".to_string()));
    assert!(is_palindrome(" ".to_string()));

    assert!(!is_palindrome("race a car".to_string()));
}
