from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    lmin, lmax = (list1, list2) if list1.val < list2.val else (list2, list1)
    lmin.next = merge_two_lists(lmin.next, lmax)

    return lmin


# def merge_two_lists(
#     list1: Optional[ListNode], list2: Optional[ListNode]
# ) -> Optional[ListNode]:
#     dummy = node = ListNode()

#     while list1 and list2:
#         if list1.val < list2.val:
#             node.next = list1
#             list1 = list1.next
#         else:
#             node.next = list2
#             list2 = list2.next
#         node = node.next

#     node.next = list1 or list2

#     return dummy.next


if __name__ == "__main__":
    l13 = ListNode(val=4)
    l12 = ListNode(val=2, next=l13)
    l11 = ListNode(val=1, next=l12)

    l23 = ListNode(val=4)
    l22 = ListNode(val=3, next=l23)
    l21 = ListNode(val=1, next=l22)

    cur = merge_two_lists(l11, l21)
    while cur:
        print(cur.val)
        cur = cur.next
