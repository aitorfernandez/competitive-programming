from typing import List
from collections import Counter


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    students = Counter(students)

    for s in sandwiches:
        if students[s]:
            students[s] -= 1
        else:
            break

    return sum(students.values())


if __name__ == "__main__":
    assert countStudents([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    assert countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
