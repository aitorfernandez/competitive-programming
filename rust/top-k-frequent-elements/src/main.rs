use std::collections::HashMap;

fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut hm: HashMap<i32, i32> = HashMap::new();

    for n in nums {
        *hm.entry(n).or_default() += 1;
    }

    let mut v: Vec<(i32, i32)> = hm.into_iter().collect();
    v.sort_by(|a, b| (b.1).cmp(&(a.1)));

    let mut res = vec![];

    for i in 0..k {
        res.push(v[i as usize].0)
    }

    res
}

fn main() {
    assert_eq!(top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2), vec![1, 2]);
    assert_eq!(top_k_frequent(vec![1], 1), vec![1]);
}
