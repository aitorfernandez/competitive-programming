use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hm: HashMap<i32, i32> = HashMap::new();

    for i in 0..nums.len() {
        let sub = target - nums[i];

        if hm.contains_key(&sub) {
            return vec![hm[&sub], i as i32];
        } else {
            hm.insert(nums[i], i as i32);
        }
    }

    vec![]
}

fn main() {
    assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
    assert_eq!(two_sum(vec![3, 2, 4], 6), vec![1, 2]);
}
