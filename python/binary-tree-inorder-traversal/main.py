from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def inorder(root: Optional[TreeNode]):
        if not root:
            return

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)

    return res


if __name__ == "__main__":
    # tree = TreeNode(1)

    # tree.right = TreeNode(2)
    # tree.right.left = TreeNode(3)

    # # root 1 is first in the result because there is not left nodes
    # assert (res := inorder_traversal(tree)) == [1, 3, 2], f"Expected [1,3,2], got {res}"

    tree = TreeNode(4)

    tree.left = TreeNode(3)
    tree.left.left = TreeNode(2)

    tree.right = TreeNode(6)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)

    assert (res := inorder_traversal(tree)) == [2, 3, 4, 5, 6, 7]
