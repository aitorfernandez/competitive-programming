# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def firstBadVersion(n: int) -> int:
    l, r = 1, n

    while r > l:
        m = l + (r - l) // 2

        if isBadVersion(m):
            r = m
        else:
            l = m + 1

    return l


if __name__ == "__main__":
    assert firstBadVersion(5) == 4
