from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    res = list(range(len(nums) * 2))

    for i in range(len(nums)):
        res[i], res[i + len(nums)] = nums[i], nums[i]

    return res


if __name__ == "__main__":
    assert get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert get_concatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
