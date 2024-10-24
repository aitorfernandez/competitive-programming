from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    q = deque()

    for c in s:
        while c in q:
            q.popleft()
        q.append(c)
        longest = max(longest, len(q))

    return longest


if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
