from typing import List


def encode(strs: List[str]) -> str:
    res = []
    for s in strs:
        res.append(f"{len(s)}:{s}")

    return "".join(res)


def decode(s: str) -> List[str]:
    l, res = 0, []

    while len(s) > l:
        separator = s.find(":", l)

        n = int(s[l:separator])
        l = separator + 1 + n

        res.append(s[separator + 1 : l])

    return res


if __name__ == "__main__":
    assert decode(encode(["neet", "code", "love", "you"])) == [
        "neet",
        "code",
        "love",
        "you",
    ]
    assert decode(encode(["we", "say", ":", "yes"])) == ["we", "say", ":", "yes"]
