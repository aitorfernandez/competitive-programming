# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guessNumber(n: int) -> int:
    l, r = 1, n

    while r >= l:
        m = l + (r - l) // 2

        res = guess(m)

        if res == 0:
            return m
        if res == 1:
            l = m + 1
        if ress == -1:
            r = m - 1


if __name__ == "__main__":
    assert guessNumber(10) == 6
    assert guessNumber(1) == 1
