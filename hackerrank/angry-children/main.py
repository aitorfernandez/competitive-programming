def max_min(k, arr):
    arr.sort()

    l, r = 0, k - 1

    total_min = float("inf")

    while r < len(arr):
        diff = arr[r] - arr[l]
        total_min = min(total_min, diff)
        l += 1
        r += 1

    return total_min


if __name__ == "__main__":
    assert max_min(2, [1, 4, 7, 2]) == 1
    assert max_min(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]) == 3
    assert max_min(2, [1, 2, 1, 2, 1]) == 0
