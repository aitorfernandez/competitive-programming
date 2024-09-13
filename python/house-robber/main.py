from typing import List


def rob(nums: List[int]) -> int:
    l, r = 0, 0

    for n in nums:
        temp = max(l + n, r)
        l = r
        r = temp

    return r


if __name__ == "__main__":
    assert (res := rob([1, 2, 3, 1]) == 4), f"Expected 4, got {res}"
    assert (res := rob([2, 7, 9, 3, 1]) == 12), f"Expected 12, got {res}"
