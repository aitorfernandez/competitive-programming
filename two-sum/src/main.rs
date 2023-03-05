pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;
    let mut hm: HashMap<i32, i32> = HashMap::with_capacity(nums.len());

    for (i, n) in nums.iter().enumerate() {
        match hm.get(&(target - n)) {
            Some(v) => return vec![*v, i as i32],
            None => hm.insert(*n, i as i32),
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
        res: Vec<i32>,
    }

    for t in vec![
        TestData {
            nums: vec![2, 7, 11, 15],
            target: 9,
            res: vec![0, 1],
        },
        TestData {
            nums: vec![5, 6, 3, 9],
            target: 8,
            res: vec![0, 2],
        },
    ] {
        let res = two_sum(t.nums, t.target);
        assert_eq!(res.len(), 2);
        assert_eq!(res, t.res);
    }
}
