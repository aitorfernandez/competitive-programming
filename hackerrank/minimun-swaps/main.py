def minimum_swaps(q):
    idx = {value: i for i, value in enumerate(q)}

    res = 0

    for i in range(len(q)):
        correct_position = i + 1

        if q[i] != correct_position:
            correct_index = idx[correct_position]

            q[i], q[correct_index] = q[correct_index], q[i]

            idx[q[correct_index]] = correct_index
            idx[q[i]] = i

            res += 1

    return res


if __name__ == "__main__":
    assert minimum_swaps([1, 3, 5, 2, 4, 6, 7]) == 3
