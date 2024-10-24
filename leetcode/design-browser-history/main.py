class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)

        # self.history = [homepage]
        # self.cur = 0

    def visit(self, url: str) -> None:
        new_node = ListNode(url, self.history)
        self.history.next = new_node
        self.history = new_node

        # self.cur += 1
        # self.history[self.cur :] = [url]

    def back(self, steps: int) -> str:
        while self.history.prev and steps > 0:
            steps -= 1
            self.history = self.history.prev
        return self.history.val

        # self.cur = max(0, self.cur - steps)
        # return self.history[self.cur]

    def forward(self, steps: int) -> str:
        while self.history.next and steps > 0:
            steps -= 1
            self.history = self.history.next
        return self.history.val

        # self.cur = min(len(self.history) - 1, self.cur + steps)
        # return self.history[self.cur]


if __name__ == "__main__":
    b = BrowserHistory("leetcode.com")

    b.visit("google.com")
    b.visit("facebook.com")
    b.visit("youtube.com")

    assert (res := b.back(1)) == "facebook.com", f"expected facebook.com, got {res}"
    assert (res := b.back(1)) == "google.com", f"expected google.com, got {res}"
    assert (res := b.forward(1)) == "facebook.com", f"expected facebook.com, got {res}"

    b.visit("linkedin.com")

    assert (res := b.forward(2)) == "linkedin.com", f"expected linkedin.com, got {res}"
    assert (res := b.back(2)) == "google.com", f"expected google.com, got {res}"
    assert (res := b.back(7)) == "leetcode.com", f"expected leetcode.com, got {res}"
