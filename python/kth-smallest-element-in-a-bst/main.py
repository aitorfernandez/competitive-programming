from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    count, res = 0, -1

    def inorder(root: Optional[TreeNode]):
        nonlocal count
        nonlocal res

        if not root:
            return

        inorder(root.left)
        count += 1
        if count == k:
            res = root.val
            return res
        inorder(root.right)

    inorder(root)
    return res


if __name__ == "__main__":
    # tree = TreeNode(3)

    # tree.left = TreeNode(1)
    # tree.left.right = TreeNode(2)

    # tree.right = TreeNode(4)

    # assert (res := kth_smallest(tree, 1)) == 1, f"Expected 1, got {res}"

    tree = TreeNode(3)

    tree.left = TreeNode(3)
    tree.right = TreeNode(6)

    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(4)

    tree.left.left.left = TreeNode(1)

    assert (res := kth_smallest(tree, 3)) == 3, f"Expected 3, got {res}"
