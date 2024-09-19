def repeated_string(s, n):
    count = s.count("a")
    total = count * (n // len(s))

    total += s[: n % len(s)].count("a")

    return total


if __name__ == "__main__":
    assert repeated_string("aba", 10) == 7
    assert repeated_string("ababa", 3) == 2
    assert (
        repeated_string(
            "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq",
            549382313570,
        )
        == 16481469408
    )
