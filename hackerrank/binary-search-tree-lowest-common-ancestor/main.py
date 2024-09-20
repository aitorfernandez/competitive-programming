class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def lca(root, v1, v2):
    while root:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root


if __name__ == "__main__":
    t = Node(4)
    t.left = Node(2)
    t.right = Node(7)

    t.left.left = Node(1)
    t.left.right = Node(3)

    t.right.left = Node(6)

    assert lca(t, 1, 7).info == 4
