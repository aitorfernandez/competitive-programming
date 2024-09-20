def luck_balance(k, contests):
    important = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            total_luck += luck

    important.sort(reverse=True)

    total_luck += sum(important[:k])
    total_luck -= sum(important[k:])

    return total_luck


if __name__ == "__main__":
    assert luck_balance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]) == 29
