def characterReplacement(s: str, k: int) -> int:
    count = {}
    l, longest, max_count = 0, 0, 0

    for r, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        max_count = max(max_count, count[c])

        if (r - l + 1) - max_count > k:
            count[s[l]] -= 1
            l += 1

        longest = max(longest, (r - l + 1))

    return longest


if __name__ == "__main__":
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("AABABBA", 1) == 4
