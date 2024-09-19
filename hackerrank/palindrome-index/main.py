def palindromeIndex(s):
    n = len(s) - 1

    for i in range(n // 2 + 1):
        if s[i] != s[n - i]:
            if s[i] == s[n - 1 - i] and s[i + 1] == s[n - 2 - i]:
                return n - i
            else:
                return i

    return -1


if __name__ == "__main__":
    # res = palindromeIndex("wasitacaroracatisaw")

    res = palindromeIndex("bcbc")
    res = palindromeIndex("quyjjdcgsvvsgcdjjyq")
    print(res)
