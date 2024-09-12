from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def backtracking(root: Optional[TreeNode]) -> List[int]:
    path = []

    def dfs(root: Optional[TreeNode]) -> bool:
        if not root or root.val == 0:
            return False

        path.append(root.val)

        if not root.left and not root.right:
            return True
        if dfs(root.left):
            return True
        if dfs(root.right):
            return True

        # if we try both subtrees (left and right) and neither leads to a solution, we need to backtrack
        path.pop()
        return False

    dfs(root)

    return path


if __name__ == "__main__":
    tree = TreeNode(4)

    tree.left = TreeNode(0)
    tree.right = TreeNode(1)

    tree.left.right = TreeNode(7)

    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(0)

    assert (res := backtracking(tree) == [4, 1, 2]), f"Expected [4,1,2], got {res}"
