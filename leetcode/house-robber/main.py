from typing import List


def rob(nums: List[int]) -> int:
    r1, r2 = 0, 0

    for n in nums:
        temp = max(n + r1, r2)
        r1 = r2
        r2 = temp

    return r2

    # recursive + memo
    # memo = {}

    # def dfs(i):
    #     if i >= len(nums):
    #         return 0
    #     if i in memo:
    #         return memo[i]

    #     # skip the current house or rob it
    #     memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
    #     return memo[i]

    # return dfs(0)


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
