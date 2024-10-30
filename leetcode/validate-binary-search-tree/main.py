from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(root, min_val, max_val):
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        return valid(root.left, min_val, root.val) and valid(
            root.right, root.val, max_val
        )

    return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)

    assert isValidBST(t) == True

    t = TreeNode(5)
    t.left = TreeNode(1)
    t.right = TreeNode(4)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(6)

    assert isValidBST(t) == False

    t = TreeNode(0)

    assert isValidBST(t) == True
