from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, subset, total):
        if total == target:
            res.append(subset.copy())
            return
        if i >= len(candidates) or total > target:
            return

        subset.append(candidates[i])
        dfs(i, subset, total + candidates[i])

        subset.pop()
        dfs(i + 1, subset, total)

    dfs(0, [], 0)

    return res


if __name__ == "__main__":
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
