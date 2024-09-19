from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    s = set()
    for n in nums:
        if n in s:
            return True
        s.add(n)

    return False


if __name__ == "__main__":
    assert (
        res := contains_duplicate([1, 2, 3, 1])
    ) == True, f"Expected True, got {res}"
    assert (
        res := contains_duplicate([1, 2, 3, 4])
    ) == False, f"Expected False, got {res}"
