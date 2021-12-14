use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    fn sort_n_lowercase(input: &str) -> String {
        let mut chars: Vec<char> = input.to_lowercase().chars().collect();
        chars.sort();
        chars.into_iter().collect()
    }

    let mut result: HashSet<&'a str> = HashSet::new();
    let sorted_word = sort_n_lowercase(word);

    for anagram in possible_anagrams {
        if anagram.to_lowercase() == word.to_lowercase() {
            continue;
        }
        let sorted_anagram = sort_n_lowercase(anagram);
        if sorted_word == sorted_anagram {
            result.insert(*anagram);
        }
    }

    result
}
