pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;

    let mut hm: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
    for (i, val) in nums.iter().enumerate() {
        match hm.get(&(target - val)) {
            Some(v) => return vec![i as i32, *v],
            None => hm.insert(*val, i as i32),
        };
    }
    vec![]
}

fn main() {
    println!("two-sum",);
}

#[test]
fn two_sum_test() {
    struct TestData {
        nums: Vec<i32>,
        target: i32,
        exp: Vec<i32>,
    }

    for t in vec![
        TestData {
            nums: vec![2, 7, 11, 15],
            target: 9,
            exp: vec![1, 0],
        },
        TestData {
            nums: vec![5, 6, 3, 9],
            target: 8,
            exp: vec![2, 0],
        },
    ] {
        let res = two_sum(t.nums, t.target);
        assert_eq!(res.len(), 2);
        assert_eq!(res, t.exp);
    }
}
