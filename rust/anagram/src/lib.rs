use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let word_lower = word.to_lowercase();
    let word_sorted = get_sorted(&word_lower);

    possible_anagrams
        .iter()
        // Creates an iterator which uses a closure to determine if an element should be yielded.
        .filter(|candidate| {
            let candidate_lower = candidate.to_lowercase();
            candidate_lower.len() == word_lower.len()
                && candidate_lower != word_lower
                && get_sorted(&candidate_lower) == word_sorted
        })
        // Creates an iterator which copies all of its elements.
        .copied()
        // Transforms an iterator into a collection.
        .collect()
}

fn get_sorted(word: &str) -> Vec<char> {
    let mut word_sorted: Vec<char> = word.chars().collect();
    word_sorted.sort_unstable();
    word_sorted
}
