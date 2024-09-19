from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)

    l, r = dummy, head
    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        r = r.next
        l = l.next

    l.next = l.next.next
    return dummy.next


if __name__ == "__main__":
    n = ListNode(1)
    n.next = ListNode(2)
    n.next.next = ListNode(3)
    n.next.next.next = ListNode(4)
    n.next.next.next.next = ListNode(5)

    n = remove_nth_from_end(n, 2)

    assert n.val == 1
    assert n.next.val == 2
    assert n.next.next.val == 3
    assert n.next.next.next.val == 5
