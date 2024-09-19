from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return

    res = []
    q = deque()
    q.append(root)

    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level)

    return res


if __name__ == "__main__":
    tree = TreeNode(3)

    tree.left = TreeNode(9)
    tree.right = TreeNode(20)

    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    assert (res := level_order(tree)) == [[3], [9, 20], [15, 7]]
