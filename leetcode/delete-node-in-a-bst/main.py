from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val
            root.right = delete_node(root.right, root.val)

    return root


if __name__ == "__main__":
    tree = TreeNode(50)

    tree.left = TreeNode(30)
    tree.left.left = TreeNode(20)
    tree.left.left.left = TreeNode(10)
    tree.left.left.left.left = TreeNode(5)

    t = delete_node(tree, 5)
    assert t.left.left.left.left == None

    # tree = TreeNode(50)

    # tree.left = TreeNode(30)
    # tree.right = TreeNode(80)

    # tree.right.left = TreeNode(60)
    # tree.right.right = TreeNode(90)

    # tree.left.left = TreeNode(20)
    # tree.left.right = TreeNode(40)

    # tree.left.right.left = TreeNode(35)
    # tree.left.right.right = TreeNode(41)

    # tree.left.left.left = TreeNode(10)
    # tree.left.left.left.left = TreeNode(5)

    # tree.left.left.right = TreeNode(25)
    # tree.left.left.right.left = TreeNode(22)
    # tree.left.left.right.right = TreeNode(26)

    # t = delete_node(tree, 20)
    # assert t.left.left.val == 22
    # assert t.left.left.right.val == 25
    # assert t.left.left.right.right.val == 26
