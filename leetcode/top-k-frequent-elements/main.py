from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # count = {}
    # for n in nums:
    #     count[n] = count.get(n, 0) + 1
    count = Counter(nums)
    values = list(count.items())
    sorted_values = sorted(values, key=lambda v: v[1], reverse=True)

    res = []
    for i in range(k):
        res.append(sorted_values[i][0])

    return res


if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert topKFrequent([1], 1) == [1]
    assert topKFrequent([1, 2], 2) == [1, 2]
