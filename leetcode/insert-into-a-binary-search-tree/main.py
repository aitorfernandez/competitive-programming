from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root


if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right = TreeNode(7)

    t = insertIntoBST(t, 5)
    assert t.right.left.val == 5
