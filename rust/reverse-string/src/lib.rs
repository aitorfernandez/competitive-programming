pub fn reverse(input: &str) -> String {
    // let mut c: Vec<char> = Vec::new();
    // for i in input.chars() {
    //     c.push(i);
    // }
    // c.reverse();
    // c.iter().collect::<String>()

    // let mut c: Vec<char> = Vec::new();
    // for i in input.chars().rev() {
    //     c.push(i);
    // }
    // c.iter().collect::<String>()

    // input.chars().rev().collect::<String>()

    input.chars().rev().collect()
}
