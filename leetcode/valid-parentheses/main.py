def is_valid(s: str) -> bool:
    res = []

    for c in s:
        if c in "([{":
            res.append(c)
        elif c == ")":
            if not res or res.pop() != "(":
                return False
        elif c == "]":
            if not res or res.pop() != "[":
                return False
        elif c == "}":
            if not res or res.pop() != "{":
                return False
        else:
            continue

    return len(res) == 0


if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{[]}") == True
    assert is_valid("(]") == False
    assert is_valid("([])") == True
