use std::cmp::Ordering::{Equal, Greater, Less};

pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
    nums.sort();

    let mut res: Vec<Vec<i32>> = Vec::new();

    for i in 0..nums.len() - 1 {
        if i > 0 && nums[i] == nums[i - 1] {
            continue;
        }

        let (mut l, mut r) = (i + 1, nums.len() - 1);

        while l < r {
            match (nums[i] + nums[l] + nums[r]).cmp(&0) {
                Less => l += 1,
                Greater => r -= 1,
                Equal => {
                    res.push(vec![nums[i], nums[l], nums[r]]);
                    l += 1;
                    while nums[l] == nums[l - 1] && l < r {
                        l += 1;
                    }
                    r -= 1;
                    while nums[r] == nums[r + 1] && l < r {
                        r -= 1;
                    }
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

    let empty: Vec<Vec<i32>> = Vec::new();
    assert_eq!(three_sum(vec![0, 1, 1]), empty);

    assert_eq!(three_sum(vec![0, 0, 0]), vec![vec![0, 0, 0]]);

    assert_eq!(three_sum(vec![-2, 0, 0, 2, 2]), vec![vec![-2, 0, 2]]);
}
