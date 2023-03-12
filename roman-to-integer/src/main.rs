pub fn roman_to_int(s: String) -> i32 {
    s.replace("IV", "IIII")
        .replace("CM", "DCCCC")
        .replace("XC", "LXXXX")
        .replace("IX", "VIIII")
        .replace("CD", "CCCC")
        .replace("XL", "XXXX")
        .chars()
        .fold(0, |mut acc, el| {
            match el {
                'I' => acc += 1,
                'V' => acc += 5,
                'X' => acc += 10,
                'L' => acc += 50,
                'C' => acc += 100,
                'D' => acc += 500,
                'M' => acc += 1000,
                _ => (),
            }
            acc
        })
}

fn main() {
    assert_eq!(roman_to_int("III".to_string()), 3);
    assert_eq!(roman_to_int("LVIII".to_string()), 58);
    assert_eq!(roman_to_int("MCMXCIV".to_string()), 1994);
}
