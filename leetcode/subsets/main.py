from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    subset, res = [], []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


if __name__ == "__main__":
    assert subsets([1, 2, 3]) == [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    assert subsets([0]) == [[0], []]
