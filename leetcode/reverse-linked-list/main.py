from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    l = reverseList(l)
    assert l.val == 5
    assert l.next.val == 4
    assert l.next.next.val == 3
    assert l.next.next.next.val == 2
    assert l.next.next.next.next.val == 1
