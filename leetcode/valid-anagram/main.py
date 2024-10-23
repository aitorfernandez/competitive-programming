def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1
        count[t[i]] = count.get(t[i], 0) - 1

    if all(v == 0 for v in count.values()):
        return True
    else:
        return False


if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
