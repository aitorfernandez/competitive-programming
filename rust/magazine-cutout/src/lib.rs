use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut m: HashMap<&str, isize> = HashMap::new();

    magazine.iter().for_each(|w| {
        *m.entry(w).or_default() += 1;
    });

    note.iter().for_each(|w| {
        *m.entry(w).or_default() -= 1;
    });

    // all() takes a closure that returns true or false
    // It applies the closure to each element of the iterator, and if they all return true, then
    // so does all().
    m.values().all(|v| *v >= 0)
}
