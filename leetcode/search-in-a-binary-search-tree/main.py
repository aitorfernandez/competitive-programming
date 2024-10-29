from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(root):
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return dfs(root.left)
        else:
            return dfs(root.right)

    return dfs(root)


if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)

    t = searchBST(t, 2)

    assert t.val == 2
    assert t.left.val == 1
    assert t.right.val == 3

    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)

    assert searchBST(t, 5) == None
