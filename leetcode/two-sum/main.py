from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    pos = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in pos:
            return [pos[diff], i]
        pos[n] = i

    return []


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
