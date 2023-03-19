# 迭代的方式遍历二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res


def inorder_traversal(root: TreeNode):
    if not root:
        return []
    stack, res = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res


def postorder_traversal(root: TreeNode):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]


def bfs(root: TreeNode):
    if not root:
        return []
    queue, res = [root], []
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
