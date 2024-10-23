from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    seq = {}

    for n in nums:
        if not n - 1 in nums:
            seq[n] = 0

            for i in range(len(nums)):
                if n + i in nums:
                    seq[n] += 1
                else:
                    break

    if not seq:
        return 0
    else:
        return max(seq.values())


if __name__ == "__main__":
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
