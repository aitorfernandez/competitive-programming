def gridChallenge(grid):
    sorted_grid = []

    for g in grid:
        sorted_grid.append("".join(sorted(g)))

    rows = len(sorted_grid)
    cols = len(sorted_grid[0])

    for col in range(cols):
        check = []
        for row in range(rows):
            check.append(sorted_grid[row][col])

        if not sorted(check) == check:
            return "NO"

    return "YES"


if __name__ == "__main__":
    grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
    assert gridChallenge(grid) == "YES"
    grid = ["mpxz", "abcd", "wlmf"]
    assert gridChallenge(grid) == "NO"
