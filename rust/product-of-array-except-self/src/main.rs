fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut res = vec![1; nums.len()];

    let mut prefix = 1;

    for i in 0..nums.len() {
        res[i] = prefix;
        prefix *= nums[i];
    }

    let mut postfix = 1;

    for i in (0..nums.len()).rev() {
        res[i] *= postfix;
        postfix *= nums[i]
    }

    res

    // let mut hm: HashMap<i32, (i32, Vec<i32>)> = HashMap::new();

    // for (i, n) in nums.iter().enumerate() {
    //     hm.entry(*n).or_insert((i as i32, nums.clone()));
    // }

    // let mut res = vec![0; nums.len()];

    // for (k, t) in hm {
    //     let mut product = 1;
    //     let (p, vv) = t;
    //     for v in vv {
    //         if v != k {
    //             product *= v;
    //         }
    //     }
    //     res[p as usize] = product;
    // }

    // res
}

fn main() {
    assert_eq!(product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6]);
    assert_eq!(
        product_except_self(vec![-1, 1, 0, -3, 3]),
        vec![0, 0, 9, 0, 0]
    );
}
