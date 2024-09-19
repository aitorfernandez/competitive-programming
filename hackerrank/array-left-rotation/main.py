def rot_left(a, d):
    r = d % len(a)
    res = a[r:]

    for i in range(r):
        res.append(a[i])

    return res


if __name__ == "__main__":
    assert rot_left([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
