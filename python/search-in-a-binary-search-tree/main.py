from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return

    if root.val == val:
        return root

    if root.val < val:
        return search_bst(root.right, val)
    else:
        return search_bst(root.left, val)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    assert search_bst(tree, 2).val == 2, "Test case 1 failed"
    assert search_bst(tree, 7).val == 7, "Test case 2 failed"
    assert search_bst(tree, 1).val == 1, "Test case 3 failed"

    assert search_bst(tree, 5) is None, "Test case 4 failed"
    assert search_bst(tree, 8) is None, "Test case 5 failed"
