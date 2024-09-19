def minimum_bribes(q):
    res = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                res += 1

    print(res)


if __name__ == "__main__":
    minimum_bribes([1, 2, 3, 4, 5])
