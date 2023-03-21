pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;

    let mut hm: HashMap<i32, i32> = HashMap::new();

    for (i, n) in nums.iter().enumerate() {
        match hm.get(&(target - n)) {
            Some(v) => return vec![*v, i as i32],
            None => {
                hm.insert(*n, i as i32);
            }
        }
    }

    vec![]
}

fn main() {
    assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
    assert_eq!(two_sum(vec![3, 2, 4], 6), vec![1, 2]);
    assert_eq!(two_sum(vec![3, 3], 6), vec![0, 1]);
}
