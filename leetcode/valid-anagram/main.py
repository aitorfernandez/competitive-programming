def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d = dict()

    for a, b in zip(s, t):
        d[a] = d.get(a, 0) + 1
        d[b] = d.get(b, 0) - 1

    return all(v == 0 for v in d.values())


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
