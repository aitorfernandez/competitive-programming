def sherlock_and_anagrams(s):
    count = {}

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            k = "".join(sorted(substring))
            count[k] = count.get(k, 0) + 1

    res = 0
    for c in count.values():
        if c > 1:
            # This represents the number of ways to choose 2 items out of count.
            res += (c * (c - 1)) // 2

    return res


if __name__ == "__main__":
    assert sherlock_and_anagrams("abba") == 4
    assert sherlock_and_anagrams("abcd") == 0
    assert sherlock_and_anagrams("cdcd") == 5
