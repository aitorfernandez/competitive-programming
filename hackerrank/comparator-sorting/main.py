from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0


if __name__ == "__main__":
    p1 = Player("smith", 20)
    p2 = Player("jones", 15)
    p3 = Player("jones", 20)

    data = [p1, p2, p3]
    data = sorted(data, key=cmp_to_key(Player.comparator))

    for i in data:
        print(i.name, i.score)
