# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def check_sub_tree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        # 是否子树：
        # 1. 两树相同
        # 2. 是左子树
        # 3. 是右子树
        return self.is_same_tree(t1, t2) or self.check_sub_tree(t1.left, t2) or self.check_sub_tree(t1.right, t2)

    def is_same_tree(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        # 两树相同
        # 1. 值相等
        # 2. 左，右子树相等
        return t1.val == t2.val and self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)
