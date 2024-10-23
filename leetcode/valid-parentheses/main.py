from collections import deque


def isValid(s: str) -> bool:
    stack = deque()

    for c in s:
        if c == ")":
            if not stack or stack.pop() != "(":
                return False
        elif c == "]":
            if not stack or stack.pop() != "[":
                return False
        elif c == "}":
            if not stack or stack.pop() != "{":
                return False
        else:
            stack.append(c)

    return len(stack) == 0


if __name__ == "__main__":
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("]") == False
