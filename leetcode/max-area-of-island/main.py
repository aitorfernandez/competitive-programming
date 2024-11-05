from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    max_area = 0

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= rows
            or c >= cols
            or (r, c) in visited
            or grid[r][c] == 0
        ):
            return 0

        visited.add((r, c))
        area = 1

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for rd, cd in directions:
            area += dfs(r + rd, c + cd)

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                area = dfs(r, c)
                max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert maxAreaOfIsland(grid) == 6

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert maxAreaOfIsland(grid) == 0
