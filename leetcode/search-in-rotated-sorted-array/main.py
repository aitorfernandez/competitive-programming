from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while r >= l:
        m = l + (r - l) // 2

        if nums[m] == target:
            return m

        if nums[m] >= nums[l]:
            if target < nums[l] or target > nums[m]:
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
