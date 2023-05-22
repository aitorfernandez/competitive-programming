pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    // let mut ans: Vec<i32> = Vec::new();

    // for _ in 0..2 {
    //     for n in nums.iter() {
    //         ans.push(*n)
    //     }
    // }

    // ans

    [nums.clone(), nums].concat()
}

fn main() {
    assert_eq!(get_concatenation(vec![1, 2, 1]), vec![1, 2, 1, 1, 2, 1]);
    assert_eq!(
        get_concatenation(vec![1, 3, 2, 1]),
        vec![1, 3, 2, 1, 1, 3, 2, 1]
    );
}
