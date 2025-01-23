fn clean(s: String) -> String {
    let res: Vec<_> = s
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_lowercase().to_string())
        .collect();

    res.into_iter().collect()
}

fn is_palindrome(s: String) -> bool {
    let chars: Vec<char> = clean(s.clone()).chars().collect();

    let mut l = 0;
    let mut r = chars.len() - 1;

    while r > l {
        if chars[l] != chars[r] {
            return false;
        }
        l += 1;
        r -= 1;
    }

    true
}

fn main() {
    assert!(is_palindrome("A man, a plan, a canal: Panama".to_string()));
}
