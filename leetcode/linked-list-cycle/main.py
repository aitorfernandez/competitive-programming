from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    l = ListNode(3)
    l.next = ListNode(2)
    l.next.next = ListNode(0)
    l.next.next.next = ListNode(-4)
    l.next.next.next.next = l.next

    assert hasCycle(l) == True

    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = l.next

    assert hasCycle(l) == True

    l = ListNode(1)

    assert hasCycle(l) == False
