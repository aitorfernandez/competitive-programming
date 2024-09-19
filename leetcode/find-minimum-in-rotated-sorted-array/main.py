from typing import List


def find_min(nums: List[int]) -> int:
    res, l, r = float("inf"), 0, len(nums) - 1

    while r >= l:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = l + (r - l) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return res


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([2, 1]) == 1
