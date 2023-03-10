pub fn longest_common_prefix(strs: Vec<&str>) -> String {
    // for w in strs.windows(2) {
    //     w[0];
    //     w[1];
    // }

    strs.iter().skip(1).fold(strs[0].to_string(), |acc, el| {
        acc.chars()
            .zip(el.chars())
            .take_while(|(a, b)| a == b)
            .map(|(a, _)| a)
            .collect()
    })
}

fn main() {
    assert_eq!(
        "fl",
        longest_common_prefix(vec!["flower", "flow", "flight"])
    );
}
