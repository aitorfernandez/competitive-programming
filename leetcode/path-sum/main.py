from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, totalSum):
        if not root:
            return False

        totalSum -= root.val
        if not root.left and not root.right:
            return totalSum == 0

        return dfs(root.left, totalSum) or dfs(root.right, totalSum)

    return dfs(root, targetSum)


if __name__ == "__main__":
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)
    t.right = TreeNode(8)

    assert hasPathSum(t, 22) == True

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)

    assert hasPathSum(t, 5) == False
