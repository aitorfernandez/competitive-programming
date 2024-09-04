fn find_min(nums: Vec<i32>) -> i32 {
    if nums.len() == 1 {
        return nums[0];
    }

    let (mut l, mut r) = (0, nums.len() - 1);

    while r > l {
        let m = l + (r - l) / 2;

        let left = nums[l];
        let mid = nums[m];
        let right = nums[r];

        if left <= mid && mid <= right {
            return left;
        } else if left >= mid && mid >= right {
            return right;
        } else if left > mid || mid < right {
            r = m;
        } else {
            l = m;
        }
    }

    -1
}

fn main() {
    assert_eq!(find_min(vec![5, 1, 2, 3, 4]), 1);

    // assert_eq!(find_min(vec![3, 4, 5, 1, 2]), 1);
    // assert_eq!(find_min(vec![4, 5, 6, 7, 0, 1, 2]), 0);
    // assert_eq!(find_min(vec![11, 13, 15, 17]), 11);
    // assert_eq!(find_min(vec![1]), 1);
}
