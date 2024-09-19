from typing import List
import math


def min_eating_speed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while r >= l:
        m = l + (r - l) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / m)

        if hours > h:
            l = m + 1
        else:
            res = min(res, m)
            r = m - 1

    return res


if __name__ == "__main__":
    assert (res := min_eating_speed([3, 6, 7, 11], 8)) == 4, f"Expected 4, got {res}"
    assert (
        res := min_eating_speed([30, 11, 23, 4, 20], 5)
    ) == 30, f"Expected 30, got {res}"
    assert (
        res := min_eating_speed([30, 11, 23, 4, 20], 6)
    ) == 23, f"Expected 30, got {res}"
