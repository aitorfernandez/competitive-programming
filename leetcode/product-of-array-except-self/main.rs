fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut res = vec![0; nums.len()];

    let mut prefix = 1;
    for i in 0..nums.len() {
        res[i] = prefix;
        prefix *= nums[i];
    }

    let mut postfix = 1;
    for i in (0..nums.len()).rev() {
        res[i] *= postfix;
        postfix *= nums[i];
    }

    res
}

fn main() {
    assert_eq!(product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6]);
}
