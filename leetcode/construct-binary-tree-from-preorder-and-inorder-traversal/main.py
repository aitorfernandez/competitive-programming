from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    m = inorder.index(preorder[0])
    root.left = build_tree(preorder[1 : m + 1], inorder[:m])
    root.right = build_tree(preorder[m + 1 :], inorder[m + 1 :])
    return root


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20

    assert tree.right.left.val == 15
    assert tree.right.right.val == 7
