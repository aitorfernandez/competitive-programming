use std::collections::{HashMap, HashSet};

fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let hs: HashSet<i32> = nums.into_iter().collect();

    let mut hm: HashMap<i32, i32> = HashMap::new();

    for n in &hs {
        if !hs.contains(&(n - 1)) {
            hm.insert(*n, 1);

            for i in 1..hs.len() {
                if hs.contains(&(n + i as i32)) {
                    hm.entry(*n).and_modify(|v| *v += 1);
                } else {
                    break;
                }
            }
        }
    }

    let res: Vec<i32> = hm.into_values().collect();
    match res.into_iter().max() {
        Some(v) => v,
        None => 0,
    }
}

fn main() {
    assert_eq!(longest_consecutive(vec![100, 4, 200, 1, 3, 2]), 4);
    assert_eq!(longest_consecutive(vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9);
}
