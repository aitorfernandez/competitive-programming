from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []

    q = deque()
    if root:
        q.append(root)

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level[-1])

    return res


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.right = TreeNode(5)
    t.right = TreeNode(3)

    assert rightSideView(t) == [1, 3, 5]
