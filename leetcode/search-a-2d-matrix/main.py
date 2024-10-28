from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

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
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
