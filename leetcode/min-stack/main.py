class MinStack:

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)
        val = min(val, self.min_values[-1] if self.min_values else val)
        self.min_values.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    s.pop()

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.top() == 3
    assert s.getMin() == 1
