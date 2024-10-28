from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while r >= l:
        m = l + (r - l) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1, 3], 3) == 1
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1
    assert search([8, 9, 2, 3, 4], 9) == 1
    assert search([3, 1], 1) == 1
