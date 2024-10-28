from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    hours = r

    while r >= l:
        m = l + (r - l) // 2

        time = 0
        for pile in piles:
            time += math.ceil(pile / m)

        if time <= h:
            hours = m
            r = m - 1
        else:
            l = m + 1

    return hours


if __name__ == "__main__":
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
