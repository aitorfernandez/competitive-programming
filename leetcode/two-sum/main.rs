use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hm: HashMap<i32, i32> = HashMap::new();

    for (i, n) in nums.into_iter().enumerate() {
        let diff = target - n;

        if hm.contains_key(&diff) {
            return vec![hm[&diff], i as i32];
        }
        hm.insert(n, i as i32);
    }

    vec![]
}

fn main() {
    assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
}
