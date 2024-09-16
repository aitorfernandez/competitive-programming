from typing import List


def max_area(heights: List[int]) -> int:
    most_water, l, r = 0, 0, len(heights) - 1

    while r > l:
        area = (r - l) * min(heights[l], heights[r])
        most_water = max(most_water, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return most_water


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
