class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        cur.val

    def add_at_head(self, val: int):
        self.add_at_index(0, val)

    def add_at_tail(self, val: int):
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int):
        if index < 0 or index > self.size:
            return

        new_node = ListNode(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next

            new_node.next = cur.next
            cur.next = new_node

        self.size += 1

    def delete_at_index(self, index: int):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next

            cur.next = cur.next.next

        self.size -= 1

    def display(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    ll = MyLinkedList()

    ll.delete_at_index(0)

    ll.add_at_head(5)
    ll.add_at_head(4)
    ll.add_at_head(3)
    ll.add_at_head(2)
    ll.add_at_head(1)

    ll.add_at_tail(0)

    ll.add_at_index(4, 32)

    ll.display()
