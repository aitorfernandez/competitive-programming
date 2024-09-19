def sock_merchant(n, ar):
    socks = {}

    for a in ar:
        socks[a] = socks.get(a, 0) + 1

    res = 0
    for _, v in socks.items():
        res += v // 2

    return res


if __name__ == "__main__":
    assert sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
