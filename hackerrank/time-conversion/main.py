def timeConversion(s):
    h = {}
    h["01"] = "13"
    h["02"] = "14"
    h["03"] = "15"
    h["04"] = "16"
    h["05"] = "17"
    h["06"] = "18"
    h["07"] = "19"
    h["08"] = "20"
    h["09"] = "21"
    h["10"] = "22"
    h["11"] = "23"

    pm = False
    if s[len(s) - 2 :] == "PM":
        pm = True

    if pm and s[:2] != "12":
        s = h[s[:2]] + s[2:]

    if not pm and s[:2] == "12":
        s = "00" + s[2 : len(s)]

    return s[: len(s) - 2]


if __name__ == "__main__":
    assert timeConversion("06:40:03PM") == "18:40:03"
    assert timeConversion("06:40:03AM") == "06:40:03"
    assert timeConversion("12:40:22AM") == "00:40:22"
    assert timeConversion("12:45:54PM") == "12:45:54"
