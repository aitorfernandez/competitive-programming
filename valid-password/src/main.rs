// You are working on an authentication system and there is a set of rules the users have to follow when picking a new password:

// 1. It has to be at least 16 characters long.
// 2. The password cannot contain the word "password". This rule is not case-sensitive.
// 3. The same character cannot be used more than 4 times. This rule is case-sensitive, "a" and "A" are different characters.
// 4. The password has to contain at least one uppercase and one lowercase letter.
// 5. The password has to contain at least one of the following special characters "*","#","@".

// Write a function that takes in a password and returns a collection of any rule numbers that are not met.

// password_1 = "Strongpwd9999#abc"             ==> []
// password_2 = "Less10#"                       ==> [1]
// password_3 = "Password@"                     ==> [1,2]
// password_4 = "#PassWord011111112222223x"     ==> [2,3]
// password_5 = "password#1111111"              ==> [2,3,4]
// password_6 = "aaaapassword$$"                ==> [1,2,3,4,5]
// password_7 = "LESS10#"                       ==> [1,4]
// password_8 = "SsSSSt#passWord"               ==> [1,2]

// 1
fn characters_long(password: &str) -> bool {
    !(password.len() >= 16)
}

// 2
fn contains_password(password: &str) -> bool {
    password.clone().to_lowercase().contains("password")
}

// 3
fn total_characters(password: &str) -> bool {
    use std::collections::HashMap;

    let mut hm: HashMap<char, u8> = HashMap::new();

    for c in password.chars() {
        hm.entry(c).and_modify(|v| *v += 1).or_insert(1);
    }

    for (_, v) in hm {
        if v > 4 {
            return true;
        }
    }

    false
}

// 4
fn uppercase_lowercase(password: &str) -> bool {
    let mut uppercase = false;
    let mut lowercase = false;

    for c in password.chars() {
        if c.is_uppercase() {
            uppercase = true;
        } else if c.is_ascii_lowercase() {
            lowercase = true;
        }
    }

    !(uppercase && lowercase)
}

// 5
fn special_characters(password: &str) -> bool {
    !(password.contains("*") || password.contains("#") || password.contains("@"))
}

fn valid_password(password: String) -> Vec<u8> {
    let mut rules = vec![];

    if characters_long(&password) {
        rules.push(1);
    }

    if contains_password(&password) {
        rules.push(2);
    }

    if total_characters(&password) {
        rules.push(3);
    }

    if uppercase_lowercase(&password) {
        rules.push(4);
    }

    if special_characters(&password) {
        rules.push(5);
    }

    rules
}

fn main() {
    assert_eq!(valid_password("Strongpwd9999#abc".to_string()), []);
    assert_eq!(valid_password("Less10#".to_string()), [1]);
    assert_eq!(valid_password("Password@".to_string()), [1, 2]);
    assert_eq!(
        valid_password("#PassWord011111112222223x".to_string()),
        [2, 3]
    );
    assert_eq!(valid_password("password#1111111".to_string()), [2, 3, 4]);
    assert_eq!(
        valid_password("aaaapassword$$".to_string()),
        [1, 2, 3, 4, 5]
    );
    assert_eq!(valid_password("LESS10#".to_string()), [1, 4]);
    assert_eq!(valid_password("SsSSSt#passWord".to_string()), [1, 2]);
}
