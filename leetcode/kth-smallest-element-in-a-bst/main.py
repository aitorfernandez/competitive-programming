from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    res, count = 0, 0

    def dfs(root):
        nonlocal res
        nonlocal count

        if not root:
            return

        dfs(root.left)
        count += 1
        if count == k:
            res = root.val
            return res
        dfs(root.right)

    dfs(root)

    return res


if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(1)
    t.left.right = TreeNode(2)
    t.right = TreeNode(4)

    assert kthSmallest(t, 1) == 1

    t = TreeNode(5)
    t.right = TreeNode(6)
    t.left = TreeNode(3)
    t.left.right = TreeNode(4)
    t.left.left = TreeNode(2)
    t.left.left.left = TreeNode(1)

    assert kthSmallest(t, 3) == 3
