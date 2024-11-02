def longestPalindrome(s: str) -> str:
    pos, longest = 0, 0
    n = len(s)
    memo = [[False] * n for _ in range(n)]

    # babad
    # range i to j
    # range 4 to 4 d d
    # range 3 to 3 a a
    # range 3 to 4 a d
    # range 2 to 2 b b
    # range 2 to 3 b a
    # range 2 to 4 b d
    # range 1 to 1 a a
    # range 1 to 2 a b
    # range 1 to 3 a a
    # range 1 to 4 a d
    # range 0 to 0 b b
    # range 0 to 1 b a
    # range 0 to 2 b b
    # range 0 to 3 b a
    # range 0 to 4 b d
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                # set to true  4 4
                # set to true  3 3
                # set to true  2 2
                # set to true  1 1
                # set to true  1 3
                # set to true  0 0
                # set to true  0 2
                memo[i][j] = True
                if longest < (j - i + 1):
                    longest = j - i + 1
                    pos = i

    return s[pos : pos + longest]

    # Brute force
    # def isPalindrome(s):
    #     l, r = 0, len(s) - 1

    #     while r > l:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1

    #     return True

    # longest = ""

    # for i in range(len(s) + 1):
    #     for j in range(i, len(s) + 1):
    #         if isPalindrome(s[i:j]):
    #             if len(longest) < len(s[i:j]):
    #                 longest = s[i:j]

    # return longest


if __name__ == "__main__":
    assert longestPalindrome("babad") == "bab" or "aba"
    assert longestPalindrome("cbbd") == "bb"
