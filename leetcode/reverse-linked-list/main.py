# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    cur, prev = head, None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


if __name__ == "__main__":
    node3 = ListNode(val=3)
    node2 = ListNode(val=2, next=node3)
    node1 = ListNode(val=1, next=node2)

    cur = reverse_list(node1)
    while cur:
        print(cur.val)
        cur = cur.next
