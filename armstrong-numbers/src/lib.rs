pub fn is_armstrong_number(num: u32) -> bool {
    // let digits = num
    //     .to_string()
    //     .chars()
    //     .map(|d| d.to_digit(10).unwrap())
    //     .collect::<Vec<_>>();

    // if digits.len() >= 10 {
    //     false
    // } else {
    //     digits
    //         .iter()
    //         .fold(0, |acc, el| acc + el.pow(digits.len() as u32))
    //         == num
    // }

    let num_str = num.to_string();
    match num_str.len() {
        0..=9 => {
            num_str
                .chars()
                .filter_map(|c| c.to_digit(10))
                .fold(0, |acc, el| acc + el.pow(num_str.len() as u32))
                == num
        }
        _ => false,
    }
}
