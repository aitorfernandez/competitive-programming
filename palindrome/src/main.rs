pub fn is_palindrome(x: i32) -> bool {
    x.to_string().chars().rev().eq(x.to_string().chars())
}

fn main() {
    assert!(is_palindrome(121));
    assert!(!is_palindrome(10));
}
