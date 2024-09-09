# class ListNode:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next


class BrowserHistory(object):

    def __init__(self, homepage: str):
        # self.history = ListNode(homepage)
        self.history = [homepage]
        self.cur = 0

    def visit(self, url: str):
        # self.history.next = ListNode(url, self.history)
        # self.history = self.history.next
        self.cur += 1
        self.history[self.cur :] = [url]

    def back(self, steps: int) -> str:
        # while self.history.prev and steps > 0:
        #     self.history = self.history.prev
        #     steps -= 1
        # return self.history.val
        self.cur = max(self.cur - steps, 0)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        # while self.history.next and steps > 0:
        #     self.history = self.history.next
        #     steps -= 1
        # return self.history.val
        self.cur = min(self.cur + steps, len(self.history) - 1)
        return self.history[self.cur]


if __name__ == "__main__":
    bh = BrowserHistory("leetcode.com")
    bh.visit("google.com")
    bh.visit("facebook.com")
    bh.visit("youtube.com")

    # bh.display()

    assert (res := bh.back(1) == "facebook.com"), f"Expect facebook.com, got {res}"
    assert (res := bh.back(1) == "google.com"), f"Expect google.com, got {res}"
    assert bh.forward(1) == "facebook.com"

    bh.visit("linkedin.com")

    assert bh.forward(2) == "linkedin.com"
    assert bh.back(2) == "google.com"
    assert bh.back(7) == "leetcode.com"
