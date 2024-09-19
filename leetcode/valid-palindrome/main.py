def is_palindrome(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    l, r = 0, len(s) - 1

    while r > l:
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
