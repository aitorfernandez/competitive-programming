def min_window(s: str, t: str) -> str:
    if len(s) == 0 or len(s) < len(t):
        return ""

    window, count = {}, {}

    for c in t:
        count[c] = count.get(c, 0) + 1

    have, need = 0, len(count)

    minimun, area, l = float("inf"), (), 0

    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1

        if c in count and window[c] == count[c]:
            have += 1

        while have == need:
            if r - l + 1 < minimun:
                area = (l, r)

            minimun = min(minimun, r - l + 1)
            window[s[l]] -= 1

            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1

            l += 1

    if len(area) == 2:
        return s[area[0] : area[1] + 1]

    return ""


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
