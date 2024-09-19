from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    cur = slow.next
    prev = slow.next = None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    l1, l2 = head, prev
    while l2:
        temp1, temp2 = l1.next, l2.next
        l1.next = l2
        l2.next = temp1
        l1 = temp1
        l2 = temp2


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    reorder_list(l)

    assert l.val == 1
    assert l.next.val == 5
    assert l.next.next.val == 2
    assert l.next.next.next.val == 4
    assert l.next.next.next.next.val == 3
