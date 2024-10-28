from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    def merge(l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next

    def merge_sort_lists(lists, l, r):
        if l == r:
            return lists[l]

        m = l + (r - l) // 2
        l1 = merge_sort_lists(lists, l, m)
        l2 = merge_sort_lists(lists, m + 1, r)

        return merge(l1, l2)

    return merge_sort_lists(lists, 0, len(lists) - 1)


if __name__ == "__main__":
    l1 = ListNode(1)

    l = mergeKLists([[], l1])

    assert l.val == 1

    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    l = mergeKLists([l1, l2, l3])

    assert l.val == 1
    assert l.next.val == 1
    assert l.next.next.val == 2
    assert l.next.next.next.val == 3
    assert l.next.next.next.next.val == 4
    assert l.next.next.next.next.next.val == 4
    assert l.next.next.next.next.next.next.val == 5
    assert l.next.next.next.next.next.next.next.val == 6
