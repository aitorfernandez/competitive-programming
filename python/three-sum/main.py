from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    res = []

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while r > l:
            s = n + nums[l] + nums[r]

            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1

    return res


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
