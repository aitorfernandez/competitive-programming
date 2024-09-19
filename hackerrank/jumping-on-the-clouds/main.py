def jumping_on_clouds(c):
    jump, r = 0, 0

    while r < len(c) - 2:
        r = r + 1 if c[r + 2] == 1 else r + 2
        jump += 1

    if r < len(c) - 1:
        jump += 1

    return jump


if __name__ == "__main__":
    assert jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]) == 4
