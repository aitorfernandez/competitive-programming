from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


if __name__ == "__main__":
    t = TreeNode(4)

    t.left = TreeNode(2)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)

    t.right = TreeNode(7)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(9)

    t = invert_tree(t)

    assert t.val == 4
    assert t.left.val == 7
    assert t.right.val == 2

    assert t.left.left.val == 9
    assert t.left.right.val == 6

    assert t.right.left.val == 3
    assert t.right.right.val == 1