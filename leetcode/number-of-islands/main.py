from typing import List


def numIslands(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= rows
            or c >= cols
            or (r, c) in visited
            or grid[r][c] == "0"
        ):
            return

        visited.add((r, c))

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for rd, cd in directions:
            dfs(r + rd, c + cd)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                islands += 1

    return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert numIslands(grid) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert numIslands(grid) == 3
