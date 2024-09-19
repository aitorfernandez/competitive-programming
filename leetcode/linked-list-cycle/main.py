from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    n = ListNode(3)
    n.next = ListNode(2)
    n.next.next = ListNode(0)
    n.next.next.next = ListNode(-4)
    n.next.next.next.next = n.next.next

    assert has_cycle(n) == True
