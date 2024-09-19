class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.lru, self.mru = ListNode(0, 0), ListNode(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert(self, node: ListNode):
        prev, nxt = self.mru.prev, self.mru
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node: ListNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    c = LRUCache(1)
    c.put(1, 1)
    assert c.get(1) == 1
