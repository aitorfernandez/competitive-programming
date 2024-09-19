def flippingMatrix(matrix):
    n = len(matrix)

    total = 0
    for row in range(n // 2):
        for col in range(n // 2):
            print(matrix[row][col])  # top left
            print(matrix[row][n - 1 - col])  # end of right
            print(matrix[n - 1 - row][col])  # bottom left
            print(matrix[n - 1 - row][n - 1 - col])  # bottom right

            total += max(
                matrix[row][col],
                max(
                    matrix[row][n - 1 - col],
                    max(matrix[n - 1 - row][col], matrix[n - 1 - row][n - 1 - col]),
                ),
            )

    print(total)


if __name__ == "__main__":
    matrix = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108],
    ]
    flippingMatrix(matrix)
