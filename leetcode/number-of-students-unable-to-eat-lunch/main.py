from typing import List
from collections import Counter


def count_students(students: List[int], sandwiches: List[int]) -> int:
    res = len(students)

    # cnt = {}
    # for s in students:
    #     if s not in cnt:
    #         cnt[s] = 0
    #     cnt[s] += 1

    # cnt = {}
    # for s in students:
    #     cnt[s] = cnt.get(s, 0) + 1

    cnt = Counter(students)

    for s in sandwiches:
        if cnt[s] > 0:
            res -= 1
            cnt[s] -= 1
        else:
            return res

    return res


if __name__ == "__main__":
    assert (
        res := count_students([1, 1, 0, 0], [0, 1, 0, 1])
    ) == 0, f"Expected 0, got {res}"
    assert (
        res := count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
    ) == 3, f"Expected 3, got {res}"
