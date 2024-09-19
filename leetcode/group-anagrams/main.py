from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    d = dict()

    for s in strs:
        key = "".join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]

    return list(d.values())


if __name__ == "__main__":
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
