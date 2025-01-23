use std::collections::HashSet;

fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut hs: HashSet<i32> = HashSet::new();

    for n in nums {
        if hs.contains(&n) {
            return true;
        }
        hs.insert(n);
    }

    false
}

fn main() {
    assert!(contains_duplicate(vec![1, 2, 3, 1]));
    assert!(!contains_duplicate(vec![1, 2, 3, 4]));
}
