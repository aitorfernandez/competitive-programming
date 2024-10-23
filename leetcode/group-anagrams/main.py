from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = {}

    for s in strs:
        k = "".join(sorted(s))
        if k in ans:
            ans[k].append(s)
        else:
            ans[k] = [s]

    return list(ans.values())


if __name__ == "__main__":
    assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert groupAnagrams([""]) == [[""]]
    assert groupAnagrams(["a"]) == [["a"]]
