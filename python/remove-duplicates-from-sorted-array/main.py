from typing import List


def remove_duplicate(nums: List[int]) -> int:
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l


if __name__ == "__main__":
    assert (res := remove_duplicate([1, 1, 2])) == 2, f"Expected 2, got {res}"
    assert (
        res := remove_duplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    ) == 5, f"Expected 5, got {res}"
