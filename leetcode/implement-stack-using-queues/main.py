from collections import deque


class MyStack:

    def __init__(self):
        # self.stack = []
        self.stack = deque()

    def push(self, x: int) -> None:
        # self.stack.append(x)
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        # return self.stack.pop()
        return self.stack.popleft()

    def top(self) -> int:
        # return self.stack[-1]
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.empty() == False
