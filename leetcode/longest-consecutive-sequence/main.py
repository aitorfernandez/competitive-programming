from typing import List


def longest_consecutive(nums: List[int]) -> int:
    nums = set(nums)
    seq = {}

    for n in nums:
        if not (n - 1) in nums:
            seq[n] = 1

            for i in range(1, len(nums)):
                if n + i in nums:
                    seq[n] += 1
                else:
                    break

    return max(seq.values())


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 1, 3, 2]) == 4
    assert (
        res := longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    ), f"Expected 9, got {res}"
