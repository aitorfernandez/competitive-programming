def isPalindrome(s: str) -> bool:
    s = "".join(c for c in s if c.isalpha() or c.isdigit()).lower()
    l, r = 0, len(s) - 1

    while r > l:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome("0P") == False
