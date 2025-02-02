fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut nums = nums.clone();
    nums.sort();

    let mut res = vec![];

    for i in 0..nums.len() {
        if i > 1 && nums[i] == nums[i - 1] {
            continue;
        }

        let mut l = i + 1;
        let mut r = nums.len() - 1;
        while r > l {
            let sum = nums[i] + nums[l] + nums[r];

            if sum < 0 {
                l += 1;
            } else if sum > 0 {
                r -= 1;
            } else {
                res.push(vec![nums[i], nums[l], nums[r]]);
                l += 1;
                r -= 1;
                while nums[l] == nums[l - 1] && l < r {
                    r += 1;
                }
            }
        }
    }

    res
}

fn main() {
    assert_eq!(
        three_sum(vec![-1, 0, 1, 2, -1, -4]),
        vec![vec![-1, -1, 2], vec![-1, 0, 1]]
    );
}
