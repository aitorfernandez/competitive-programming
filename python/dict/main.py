if __name__ == "__main__":
    d = dict()  # or d = {}

    d[1] = 1

    if 1 in d:
        print("contains 1")

    print(d[1])
    print(d.get(1))

    # hashmap.entry(x).and_modify(|v|v+=1).or_insert(1)
    d[1] = d.get(1, 0) + 1

    # *hashmap.entry(x).or_default() += 1;
    d.setdefault(2, 0)
    d[2] += 1

    d.pop(2)  # or del d[2]

    len(d) == 0  # or not d

    for k, v in d.items():
        print(k, v)

    for item in d.items():
        print(item)

    for k in d.keys():
        print(k)

    for v in d.values():
        print(v)

    d[2] = 22

    for k in d.copy():
        if d[k] == 22:
            d[k] = 2

    print(d)
