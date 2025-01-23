use std::collections::{HashMap, HashSet};

fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let hs: HashSet<i32> = HashSet::from_iter(nums);

    let mut hm: HashMap<i32, i32> = HashMap::new();

    for n in hs.iter() {
        if !hs.contains(&(n - 1)) {
            hm.insert(*n, 1);

            for i in 1..hs.len() {
                if hs.contains(&(n + i as i32)) {
                    // hm.entry(*n).and_modify(|v| *v += 1).or_insert(0);
                    if let Some(value) = hm.get_mut(n) {
                        *value += 1;
                    }
                }
            }
        }
    }

    let values: Vec<i32> = hm.into_values().collect();

    if let Some(v) = values.iter().max() {
        return *v;
    } else {
        0
    }
}

fn main() {
    assert_eq!(longest_consecutive(vec![100, 4, 200, 1, 1, 3, 2]), 4);
}
