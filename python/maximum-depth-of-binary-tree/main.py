from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    assert max_depth(t) == 3
