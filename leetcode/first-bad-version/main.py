def is_bad_version(version: int) -> bool:
    pass


def first_bad_version(self, n: int) -> int:
    l, r = 1, n

    while r > l:
        m = l + (r - l) // 2
        if is_bad_version(m):
            # if m cannot be the solution r = m - 1
            r = m
        else:
            l = m + 1

    return l


if __name__ == "__main__":
    assert (res := first_bad_version(5)) == 4, f"Expected 4, got {res}"
