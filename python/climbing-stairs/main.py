def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


if __name__ == "__main__":
    assert (res := climb_stairs(2) == 2), f"Expected 2, got {res}"
    assert (res := climb_stairs(3) == 3), f"Expected 3, got {res}"
