class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    cur = root

    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur


if __name__ == "__main__":
    t = TreeNode(6)
    t.left = TreeNode(2)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(4)
    t.left.right.left = TreeNode(3)
    t.left.right.right = TreeNode(5)
    t.right = TreeNode(8)
    t.right.left = TreeNode(7)
    t.right.right = TreeNode(9)

    assert lowestCommonAncestor(t, TreeNode(2), TreeNode(8)).val == 6
