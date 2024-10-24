from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    l, r = 0, len(height) - 1

    while r > l:
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
