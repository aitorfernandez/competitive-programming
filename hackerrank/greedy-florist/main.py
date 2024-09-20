def get_minimum_cost(k, c):
    c.sort(reverse=True)

    total_cost = 0
    purchase_rounds = [0] * k

    for i in range(len(c)):
        person = i % k
        total_cost += (purchase_rounds[person] + 1) * c[i]
        purchase_rounds[person] += 1

    return total_cost


if __name__ == "__main__":
    assert get_minimum_cost(3, [2, 5, 6]) == 13
