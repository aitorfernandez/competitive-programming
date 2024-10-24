from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n, res = len(nums), []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while r > l:
            total = nums[i] + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


if __name__ == "__main__":
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
