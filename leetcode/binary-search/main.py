from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while r >= l:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m

        if nums[m] < target:
            l = m + 1
        else:
            r = r - 1

    return -1


if __name__ == "__main__":
    assert (res := search([-1, 0, 3, 5, 9, 12], 9)) == 4, f"Expected 4, got {res}"
    assert (res := search([-1, 0, 3, 5, 9, 12], 2)) == -1, f"Expected -1, got {res}"
    assert (res := search([-1, 0, 5], 5)) == 2, f"Expected 2, got {res}"
    assert (res := search([5], 5)) == 0, f"Expected 0, got {res}"
