import string


def caesarCipher(s, k):
    # a = [chr(i) for i in range(97, 123)]
    a = list(string.ascii_lowercase)
    d = {}
    for i, c in enumerate(a):
        d[c] = i

    res = ""
    for c in s:
        if not c.isalnum() or c.isnumeric():
            res += c
        else:
            p = d[c.lower()]
            m = (p + k) % len(a)

            if c.isupper():
                res += a[m].upper()
            else:
                res += a[m]

    return res


if __name__ == "__main__":
    assert caesarCipher("middle-Outz", 2) == "okffng-Qwvb"
    assert caesarCipher("www.abc.xy", 87) == "fff.jkl.gh"
    assert caesarCipher("159357lcfd", 98) == "159357fwzx"
