fn longest_consecutive(nums: Vec<i32>) -> i32 {
    use std::collections::{HashMap, HashSet};

    let mut hm: HashMap<i32, i32> = HashMap::new();
    let hs: HashSet<i32> = nums.into_iter().collect();

    for n in &hs {
        if !hs.contains(&(*n - 1)) {
            hm.entry(*n).or_insert(1);

            for i in 1..hs.len() {
                if hs.contains(&(*n + i as i32)) {
                    hm.entry(*n).and_modify(|v| *v += 1);
                } else {
                    break;
                }
            }
        }
    }

    // let v: Vec<_> = hm.values().collect();
    // **v.iter().max().unwrap()

    let v = hm.values().collect::<Vec<&i32>>();

    if let Some(v) = v.iter().max() {
        **v
    } else {
        0
    }
}

fn main() {
    assert_eq!(longest_consecutive(vec![100, 4, 200, 1, 3, 2]), 4);
    assert_eq!(longest_consecutive(vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9);
    assert_eq!(
        longest_consecutive(vec![9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]),
        7
    );
}
