fn search(nums: Vec<i32>, target: i32) -> i32 {
    // let (mut l, mut r) = (0, nums.len() - 1);

    // for evalute vec of size 1 as assert_eq!(search(vec![5], 5), 0);
    let (mut l, mut r) = (0, nums.len());

    while r > l {
        let m = l + (r - l) / 2;

        if nums[m] == target {
            return m as i32;
        }

        if nums[m] < target {
            l = m + 1;
        } else {
            r = m;
        }
    }

    -1
}

fn main() {
    assert_eq!(search(vec![-1, 0, 3, 5, 9, 12], 9), 4);
    assert_eq!(search(vec![-1, 0, 3, 5, 9, 12], 2), -1);
    assert_eq!(search(vec![5], 5), 0);
    assert_eq!(search(vec![2, 5], 2), 0);
}
