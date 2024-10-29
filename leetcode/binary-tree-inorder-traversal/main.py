from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(root):
        if not root:
            return

        dfs(root.left)
        res.append(root.val)
        dfs(root.right)

    dfs(root)
    return res


if __name__ == "__main__":
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    assert inorderTraversal(t) == [1, 3, 2]
