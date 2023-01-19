fn main() {
    println!("palindrome");
}

pub fn is_palindromo(n: i32) -> bool {
    // n.to_string().chars().rev().eq(n.to_string().chars())

    //
    // Without use to_string
    //
    if n < 0 {
        return false;
    }

    let mut digits = Vec::new();
    let mut n = n;
    while n > 9 {
        digits.push(n % 10);
        n = n / 10;
    }
    digits.push(n);

    let cln = digits.clone();
    digits.reverse();

    cln == digits
}

#[test]
fn is_palindrome_test() {
    struct TestData {
        input: i32,
        output: bool,
    }

    for t in vec![
        TestData {
            input: 121,
            output: true,
        },
        TestData {
            input: -121,
            output: false,
        },
        TestData {
            input: 10,
            output: false,
        },
        TestData {
            input: 1001,
            output: true,
        },
    ] {
        let res = is_palindromo(t.input);
        assert_eq!(res, t.output);
    }
}
