from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    t = TreeNode(preorder[0])
    m = inorder.index(preorder[0])

    t.left = buildTree(preorder[1 : m + 1], inorder[:m])
    t.right = buildTree(preorder[m + 1 :], inorder[m + 1 :])

    return t


if __name__ == "__main__":
    t = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

    assert t.val == 3
    assert t.left.val == 9
    assert t.right.val == 20
    assert t.right.left.val == 15
    assert t.right.right.val == 7
