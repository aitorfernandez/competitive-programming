def two_strings(s1, s2):
    d = {}
    for s in s1:
        d[s] = d.get(s, 0) + 1

    for s in s2:
        if s in s1:
            return "YES"

    return "NO"


if __name__ == "__main__":
    assert two_strings("hello", "world") == "YES"
    assert two_strings("hi", "world") == "NO"
    assert two_strings("aardvark", "apple") == "YES"
