use std::cmp::Ordering::{Equal, Greater, Less};

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let (mut l, mut r) = (0, nums.len() - 1);

    while l < r {
        match (nums[l] + nums[r]).cmp(&target) {
            Less => l += 1,
            Greater => r -= 1,
            Equal => return vec![l as i32 + 1, r as i32 + 1],
        }
    }

    unreachable!()
}

// pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
//     let mut l = 0;
//     let mut r = nums.len() - 1;

//     while l < r {
//         let sum = nums[l] + nums[r];
//         if sum > target {
//             r -= 1;
//         } else if sum < target {
//             l += 1;
//         } else {
//             return vec![1 + l as i32, 1 + r as i32];
//         }
//     }

//     vec![]
// }

fn main() {
    assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![1, 2]);
    assert_eq!(two_sum(vec![2, 3, 4], 6), vec![1, 3]);
    assert_eq!(two_sum(vec![-1, 0], -1), vec![1, 2]);
}
