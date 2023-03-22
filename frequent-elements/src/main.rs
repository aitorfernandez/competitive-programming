pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    use std::collections::HashMap;

    if nums.len() as i32 == k {
        return nums;
    }

    let mut hm: HashMap<i32, i32> = HashMap::new();

    for n in nums {
        hm.entry(n).and_modify(|v| *v += 1).or_insert(1);
    }

    let mut values: Vec<(i32, i32)> = hm.into_iter().collect();
    values.sort_by(|a, b| b.1.cmp(&a.1));

    let mut res = vec![];

    for i in 0..k {
        res.push(values[i as usize].0)
    }

    res
}

fn main() {
    assert_eq!(top_k_frequent(vec![4, 1, -1, 2, -1, 2, 3], 2), vec![-1, 2]);
    assert_eq!(top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2), vec![1, 2]);
    assert_eq!(top_k_frequent(vec![1], 1), vec![1]);
    assert_eq!(top_k_frequent(vec![1, 2], 2), vec![1, 2]);
}
