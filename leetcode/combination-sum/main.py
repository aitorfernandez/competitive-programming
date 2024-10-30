from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        #          .
        #      [2]   []
        # [2,2]   [2]
        # first decission, always include same i position
        dfs(i, cur, total + candidates[i])

        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


if __name__ == "__main__":
    assert combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
