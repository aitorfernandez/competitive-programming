from typing import List


def encode(strs: List[str]) -> str:
    res = []
    for s in strs:
        res.append(f"{len(s)}:{s}")

    return "".join(res)


def decode(s: str) -> List[str]:
    l = 0
    res = []

    while l < len(s):
        i = s.find(":", l)
        p = int(s[l:i])

        res.append(s[i + 1 : i + p + 1])

        l = i + p + 1

    return res


if __name__ == "__main__":
    v = ["we", "say", ":", "1es"]

    encode_str = encode(v)
    assert decode(encode_str) == v
