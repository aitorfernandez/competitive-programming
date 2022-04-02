pub fn is_armstrong_number(num: u32) -> bool {
    let num_str: String = num.to_string();
    num_str
        .chars()
        .filter_map(|c| c.to_digit(10))
        .map(|n| n.pow(num_str.len() as u32))
        .sum::<u32>()
        == num
}
