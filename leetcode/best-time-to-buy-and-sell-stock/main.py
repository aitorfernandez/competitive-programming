from typing import List


def maxProfit(prices: List[int]) -> int:
    l, profit = 0, 0

    for r in range(1, len(prices)):
        if prices[l] < prices[r]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r

    return profit


if __name__ == "__main__":
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 9
