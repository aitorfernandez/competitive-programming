from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = dict()

    for n in nums:
        count[n] = count.get(n, 0) + 1

    freq = list(count.items())
    freq.sort(key=lambda v: v[1], reverse=True)

    res = []
    for i in range(k):
        res.append(freq[i][0])

    return res


if __name__ == "__main__":
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
