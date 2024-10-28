from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    min_element = float("inf")

    while r > l:
        m = l + (r - l) // 2
        min_element = min(min_element, nums[m])

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1

    return min(min_element, nums[l])


if __name__ == "__main__":
    assert findMin([3, 4, 5, 1, 2]) == 1
    assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert findMin([11, 13, 15, 17]) == 11
    assert findMin([3, 1, 2]) == 1
