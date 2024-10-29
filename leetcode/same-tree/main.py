from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (
        p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    )


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)

    assert isSameTree(t1, t2) == True

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(2)

    assert isSameTree(t1, t2) == False
