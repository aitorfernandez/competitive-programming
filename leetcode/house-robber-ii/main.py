from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    memo = {}

    def dfs(i, flag):
        if i >= len(nums) or (flag and i == len(nums) - 1):
            return 0

        key = (i, flag)
        if key in memo:
            return memo[key]

        memo[key] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
        return memo[key]

    return max(dfs(0, True), dfs(1, False))


if __name__ == "__main__":
    assert rob([2, 3, 2]) == 3
    assert rob([1, 2, 3, 1]) == 4
    assert rob([1, 3]) == 3
    assert rob([1, 2, 3]) == 3
    assert rob([1]) == 1
