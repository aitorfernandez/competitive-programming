from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    # s = set(nums)
    # return len(s) != len(nums)

    s = set()

    for n in nums:
        if n in s:
            return True
        s.add(n)

    return False


if __name__ == "__main__":
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
