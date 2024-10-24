class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None

        if index == 0:
            self.head = ListNode(val, self.head)
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = ListNode(val, cur.next)

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.size -= 1

    def display(self) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    l = MyLinkedList()

    l.addAtHead(1)
    l.addAtTail(3)
    l.addAtIndex(1, 2)
    assert l.get(1) == 2
    l.deleteAtIndex(1)
    assert l.get(1) == 3

    l = MyLinkedList()

    l.addAtHead(7)
    l.addAtHead(2)
    l.addAtHead(1)
    l.addAtIndex(3, 0)
    l.deleteAtIndex(2)
    l.addAtHead(6)
    l.addAtTail(4)

    assert l.get(4) == 4

    l.addAtHead(4)
    l.addAtIndex(5, 0)
    l.addAtHead(6)
