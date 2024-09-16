from typing import List


def max_profit(prices: List[int]) -> int:
    profit, l = 0, 0

    for r in range(1, len(prices)):
        if prices[l] < prices[r]:
            profit = max(profit, prices[r] - prices[l])
        else:
            l = r

    return profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
