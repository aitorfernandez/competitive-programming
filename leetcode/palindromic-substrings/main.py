def countSubstrings(s: str) -> int:
    count, n = 0, len(s)
    memo = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                memo[i][j] = True
                count += 1

    return count


if __name__ == "__main__":
    # # "a", "b", "c"
    # assert countSubstrings("abc") == 3
    # # "a", "a", "a", "aa", "aa", "aaa"
    # assert countSubstrings("aaa") == 6

    assert countSubstrings("aaaaa") == 15
