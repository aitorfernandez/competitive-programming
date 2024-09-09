from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    d = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in d:
            return [d[diff], i]
        else:
            d[n] = i

    return []


if __name__ == "__main__":
    assert (res := two_sum([2, 7, 11, 15], 9)) == [0, 1], f"Expected [0,1], got {res}"
    assert (res := two_sum([3, 2, 4], 6)) == [1, 2], f"Expected [1,2], got {res}"
