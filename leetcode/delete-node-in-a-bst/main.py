from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left)
    elif key > root.val:
        root.right = deleteNode(root.right)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = deleteNode(root.right, cur.val)

    return root


if __name__ == "__main__":
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.right = TreeNode(6)

    t.left.left = TreeNode(2)
    t.left.right = TreeNode(4)

    t.right.right = TreeNode(7)

    t = deleteNode(t, 3)

    assert t.left.val == 4
