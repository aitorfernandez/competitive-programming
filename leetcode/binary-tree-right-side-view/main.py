from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
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

        res.append(level[-1])

    return res


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(5)
    tree.right.right = TreeNode(4)

    assert (res := right_side_view(tree)) == [1, 3, 4]

    tree = TreeNode(1)
    tree.left = TreeNode(2)

    assert (res := right_side_view(tree)) == [1, 2], f"Expected [1,2], got {res}"

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)

    assert (res := right_side_view(tree)) == [1, 3, 4], f"Expected [1,3,4], got {res}"
