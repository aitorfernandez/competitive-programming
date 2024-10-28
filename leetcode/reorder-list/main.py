from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    l2 = slow.next
    slow.next = None

    prev, cur = None, l2
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    l1, l2 = head, prev
    while l1 and l2:
        temp_l1 = l1.next
        temp_l2 = l2.next

        l1.next = l2
        l2.next = temp_l1
        l2 = temp_l2
        l1 = temp_l1


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)

    reorderList(l)

    assert l.val == 1
    assert l.next.val == 4
    assert l.next.next.val == 2
    assert l.next.next.next.val == 3

    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    reorderList(l)

    assert l.val == 1
    assert l.next.val == 5
    assert l.next.next.val == 2
    assert l.next.next.next.val == 4
    assert l.next.next.next.next.val == 3
