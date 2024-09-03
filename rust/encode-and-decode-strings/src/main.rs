fn encode(strs: Vec<String>) -> String {
    let mut res: String = "".to_string();

    for s in strs {
        res.push_str(&format!("{}{}", s.len(), s));
    }

    res
}

fn decode(s: String) -> Vec<String> {
    let (mut res, mut l) = (vec![], 0);

    let cc: Vec<char> = s.chars().collect();

    while cc.len() > l {
        let len = cc[l].to_digit(10).unwrap() as usize;
        let slice = &cc[l + 1..l + 1 + len];
        res.push(slice.into_iter().collect());

        l += len + 1;
    }

    res
}

fn main() {
    let list = vec![
        "we".to_string(),
        "say".to_string(),
        ":".to_string(),
        "1es".to_string(),
    ];
    let str = encode(list.clone());
    assert_eq!(decode(str.clone()), list);
}
