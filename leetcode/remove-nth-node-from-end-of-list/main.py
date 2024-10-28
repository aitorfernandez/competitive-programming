from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    while n > 0:
        fast = fast.next
        n -= 1

    dummy = ListNode(0, head)

    cur = dummy
    while fast:
        cur = cur.next
        fast = fast.next

    cur.next = cur.next.next

    return dummy.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    l = removeNthFromEnd(l, 2)

    assert l.val == 1
    assert l.next.val == 2
    assert l.next.next.val == 3
    assert l.next.next.next.val == 5

    l = ListNode(1)
    l.next = ListNode(2)

    l = removeNthFromEnd(l, 1)

    assert l.val == 1

    l = ListNode(1)

    l = removeNthFromEnd(l, 1)

    assert l == None
