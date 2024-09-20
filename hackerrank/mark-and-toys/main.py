def maximum_toys(prices, k):
    prices.sort()
    total = 0
    count = 0

    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break

    return count


if __name__ == "__main__":
    assert maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50) == 4
