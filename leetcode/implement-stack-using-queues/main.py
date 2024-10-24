from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) + 1):
            self.q.appendleft(self.q.pop())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    s = MyStack()

    s.push(1)
    s.push(2)

    assert s.top() == 2
    assert s.pop() == 2

    assert s.empty() == False

    s = MyStack()

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.top() == 3
