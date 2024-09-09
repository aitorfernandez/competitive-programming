def guess(n: int) -> int:
    pass


def guess_number(n: int) -> int:
    l, r = 1, n

    while True:
        m = l + (r - l) // 2
        res = guess(m)

        if res == 0:
            return m
        elif res == 1:
            l = m + 1
        else:
            r = m - 1


if __name__ == "__main__":
    assert (res := guess_number(10)) == 6, f"Expected 6, got {res}"
    assert (res := guess_number(1)) == 1, f"Expected 1, got {res}"
    assert (res := guess_number(2)) == 1, f"Expected 1, got {res}"
