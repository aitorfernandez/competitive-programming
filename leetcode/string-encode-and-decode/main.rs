fn encode(strs: Vec<String>) -> String {
    let mut res = String::new();
    for s in strs {
        res.push_str(&format!("{}:{s}", s.len()));
    }

    res

    // let mut res: Vec<String> = vec![];

    // for s in strs {
    //     res.push(format!("{}:{s}", s.len()));
    // }

    // res.into_iter().collect()
}

fn decode(s: String) -> Vec<String> {
    let mut res: Vec<String> = vec![];
    let mut l: usize = 0;

    while l < s.len() {
        if let Some(separator) = s[l..].find(':') {
            let separator = l + separator;
            let n: usize = s[l..separator].parse().expect("Invalid length");

            l = separator + 1;

            res.push(s[l..l + n].to_string());

            l += n;
        } else {
            break;
        }
    }

    res
}

fn main() {
    let words = vec![
        "we".to_string(),
        "say".to_string(),
        ":".to_string(),
        "yes".to_string(),
    ];
    let s = encode(words.clone());

    assert_eq!(decode(s), words);
}
