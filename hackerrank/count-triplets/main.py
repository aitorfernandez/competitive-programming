from collections import defaultdict


def count_triplets(arr, r):
    left = defaultdict(int)
    right = defaultdict(int)

    for n in arr:
        right[n] += 1

    triplets = 0

    for j in arr:
        right[j] -= 1

        if j % r == 0:
            i = j // r
            k = j * r
            triplets += left[i] * right[k]

        left[j] += 1

    return triplets


if __name__ == "__main__":
    assert count_triplets([1, 2, 2, 4], 2) == 2
    assert count_triplets([1, 3, 9, 9, 27, 81], 3) == 6
