fn contains_duplicate(nums: Vec<i32>) -> bool {
    use std::collections::HashSet;

    let mut hs = HashSet::new();

    for n in nums {
        if hs.contains(&n) {
            return true;
        }
        hs.insert(n);
    }

    false

    //
    //
    //

    // use std::collections::HashMap;

    // let mut hm = HashMap::new();

    // // Iterate over nums and saving the values in the HashMap
    // for n in nums {
    //     hm.entry(n).and_modify(|v| *v += 1).or_insert(1);
    // }

    // // Check HashMap if any value is at least 2
    // for (_, v) in hm {
    //     if v >= 2 {
    //         return true;
    //     }
    // }
    // false
}

fn main() {
    assert!(contains_duplicate(vec![1, 2, 3, 1]));
    assert!(contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));

    assert!(!contains_duplicate(vec![1, 2, 3, 4]));
}
