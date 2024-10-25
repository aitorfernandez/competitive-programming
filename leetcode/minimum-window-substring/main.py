from collections import Counter


def minWindow(s: str, t: str) -> str:
    window = {}
    count = Counter(t)

    l, min_area, area = 0, float("inf"), (-1, -1)
    have, need = 0, len(count)

    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1

        if c in count and window[c] == count[c]:
            have += 1

        while have == need:
            if (r - l + 1) < min_area:
                area = (l, r)
                min_area = r - l + 1

            window[s[l]] -= 1
            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1
            l += 1

    return s[area[0] : area[1] + 1]


if __name__ == "__main__":
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
