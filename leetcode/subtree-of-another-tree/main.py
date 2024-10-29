from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        return (
            p.val == q.val
            and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right)
        )

    if not subRoot:
        return True
    if not root:
        return False

    return (
        isSameTree(root, subRoot)
        or isSubtree(root.left, subRoot)
        or isSubtree(root.right, subRoot)
    )


if __name__ == "__main__":
    s = TreeNode(4)
    s.left = TreeNode(1)
    s.right = TreeNode(1)

    r = TreeNode(3)
    r.right = TreeNode(5)
    r.left = s

    assert isSubtree(r, s) == True
