from typing import List
from collections import deque


def length_of_longest_substring(s: str) -> int:
    longest = 0
    q = deque()

    for c in s:
        while c in q:
            q.popleft()

        q.append(c)
        longest = max(longest, len(q))

    return longest


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
