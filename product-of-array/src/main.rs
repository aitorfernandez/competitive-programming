fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut res = vec![1];

    for i in 0..nums.len() - 1 {
        res.push(nums[i] * res[i]);
    }

    let mut prefix = 1;

    for i in (1..nums.len()).rev() {
        prefix = nums[i] * prefix;
        res[i - 1] = res[i - 1] * prefix;
    }

    res
}

fn main() {
    assert_eq!(product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6]);
    assert_eq!(
        product_except_self(vec![-1, 1, 0, -3, 3]),
        vec![0, 0, 9, 0, 0]
    );
    assert_eq!(product_except_self(vec![2, 3, 5, 0]), vec![0, 0, 0, 30]);
    assert_eq!(
        product_except_self(vec![4, 3, 2, 1, 2]),
        vec![12, 16, 24, 48, 24]
    );
}
