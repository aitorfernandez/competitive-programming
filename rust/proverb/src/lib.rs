pub fn build_proverb(list: &[&str]) -> String {
    // if list.len() == 0 {
    //     String::new()
    // } else {
    //     let mut s: String = "".to_string();
    //     for l in 0..list.len() - 1 {
    //         s = format!(
    //             "{}For want of a {} the {} was lost.\n",
    //             s,
    //             list[l],
    //             list[l + 1],
    //         );
    //     }
    //     format!("{}And all for the want of a {}.", s, list[0])
    // }

    if list.len() == 0 {
        return String::new();
    }

    list.windows(2)
        .map(|w| format!("For want of a {} the {} was lost.", w[0], w[1]))
        .chain(std::iter::once(format!(
            "And all for the want of a {}.",
            list[0]
        )))
        .collect::<Vec<_>>()
        .join("\n")
}
