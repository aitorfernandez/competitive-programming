from typing import List


def remove_element(nums: List[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1

    return l


if __name__ == "__main__":
    assert (res := remove_element([3, 2, 2, 3], 3)) == 2, f"Expected 2, got {res}"
    assert (
        res := remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
    ) == 5, f"Expected 5, got {res}"