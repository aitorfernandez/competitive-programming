from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: Optional[TreeNode]):
    if not root:
        return

    level = 0

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        print("level:", level)

        for i in range(len(queue)):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        level += 1


if __name__ == "__main__":
    tree = TreeNode(4)

    tree.left = TreeNode(3)
    tree.right = TreeNode(6)

    tree.left.left = TreeNode(2)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)

    bfs(tree)
