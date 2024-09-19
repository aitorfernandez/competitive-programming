from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def dfs(root: Optional[TreeNode], current_sum: int) -> bool:
        if not root:
            return False

        current_sum -= root.val

        if not root.left and not root.right:
            return current_sum == 0

        return dfs(root.left, current_sum) or dfs(root.right, current_sum)

    return dfs(root, target_sum)


if __name__ == "__main__":
    tree = TreeNode(5)

    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)

    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)

    assert (res := has_path_sum(tree, 22) == True), f"Expected True, got {res}"

    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    assert (res := has_path_sum(tree, 5) == False), f"Expected False, got {res}"
