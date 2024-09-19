def alternating_characters(s):
    l = 0
    w = s[l]

    for r in range(1, len(s)):
        if s[r] != w[l]:
            w += s[r]
            l += 1

    return len(s) - len(w)


if __name__ == "__main__":
    assert alternating_characters("AAAA") == 3
    assert alternating_characters("BBBBB") == 4
    assert alternating_characters("ABABABAB") == 0
