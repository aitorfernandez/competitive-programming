from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    max_path = float("-inf")

    def dfs(root):
        nonlocal max_path

        if not root:
            return 0

        path_left = dfs(root.left)
        path_right = dfs(root.right)
        max_left = max(path_left, 0)
        max_right = max(path_right, 0)

        max_path = max(max_path, (root.val + max_left + max_right))
        return root.val + max(max_left, max_right)

    dfs(root)
    return max_path


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)

    assert maxPathSum(t) == 6

    t = TreeNode(-10)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    assert maxPathSum(t) == 42

    t = TreeNode(1)

    assert maxPathSum(t) == 1

    t = TreeNode(-3)

    assert maxPathSum(t) == -3

    t = TreeNode(1)
    t.left = TreeNode(2)

    assert maxPathSum(t) == 3

    t = TreeNode(2)
    t.left = TreeNode(-1)

    assert maxPathSum(t) == 2
