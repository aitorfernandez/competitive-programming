from collections import Counter


def is_valid(s):
    count = Counter(s)
    freq = Counter(count.values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        (f1, c1), (f2, c2) = sorted(freq.items())

        if f1 == 1 and c1 == 1:
            return "YES"

        if f2 - f1 == 1 and c2 == 1:
            return "YES"

    return "NO"


if __name__ == "__main__":
    assert is_valid("abcdefghhgfedecba") == "YES"
    assert is_valid("aabbccddeefghi") == "NO"
    assert is_valid("a") == "YES"
    assert is_valid("aabbc") == "YES"
