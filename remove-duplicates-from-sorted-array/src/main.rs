pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    let mut l = 1;

    for r in 1..nums.len() {
        if nums[r] != nums[r - 1] {
            nums[l] = nums[r];
            l += 1;
        }
    }

    l as i32

    // let (mut l, mut r) = (1, 1);

    // while r < nums.len() {
    //     if nums[r] == nums[r - 1] {
    //         r += 1;
    //     } else {
    //         nums[l] = nums[r];
    //         r += 1;
    //         l += 1;
    //     }
    // }

    // println!("{nums:?}");

    // l as i32
}

fn main() {
    let mut v = vec![1, 1, 2];

    assert_eq!(remove_duplicates(&mut v), 2);
}
