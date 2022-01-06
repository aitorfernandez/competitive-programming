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

    // all() takes a closure that returns true or false.
    // It applies this closure to each element of the iterator, and if they all return true, then so does all().
    // If any of them return false, it returns false.
    map.values().all(|v| *v >= 0)
}
