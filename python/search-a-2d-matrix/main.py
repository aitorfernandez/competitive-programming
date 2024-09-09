from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    l, r = 0, (rows * cols) - 1

    while r >= l:
        m = l + (r - l) // 2

        row = m // cols
        col = m % cols

        if matrix[row][col] == target:
            return True

        if matrix[row][col] < target:
            l = m + 1
        else:
            r = m - 1

    return False


if __name__ == "__main__":
    assert (
        res := search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    ) == True, f"Expected True, got {res}"
    assert (
        res := search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    ) == False, f"Expected False, got {res}"
    assert (res := search_matrix([[1]], 2)) == False, f"Expected False, got {res}"
