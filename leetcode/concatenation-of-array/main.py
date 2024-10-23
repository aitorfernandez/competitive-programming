from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    l, res = len(nums), [0] * (len(nums) * 2)

    for i in range(l):
        res[i] = res[i + l] = nums[i]

    return res


if __name__ == "__main__":
    assert getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
