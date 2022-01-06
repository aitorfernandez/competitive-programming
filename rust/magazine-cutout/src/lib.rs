#![allow(unused)]

use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut map: HashMap<&str, isize> = HashMap::new();

    magazine.iter().for_each(|w| {
        *map.entry(w).or_default() += 1;
    });

    note.iter().for_each(|w| {
        *map.entry(w).or_default() -= 1;
    });

    map.values().all(|v| *v >= 0)
}
