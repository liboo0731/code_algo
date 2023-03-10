# 前中后序遍历 - 递归
# 层序遍历 - 队列

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def level_order(root: TreeNode):
        resl = list()
        if root is None:
            return resl

        queue_list = list()
        # 每一层从左到右依次加入队列
        queue_list.append(root)

        while queue_list:
            # 当前层节点个数
            queue_len = len(queue_list)
            # 记录当前层的值
            level_list = list()
            # 依次遍历当前层
            for i in range(queue_len):
                # 当前层依次出队列
                node = queue_list.pop(0)
                # 记录值
                level_list.append(node.val)
                if node.left:
                    queue_list.append(node.left)
                if node.right:
                    queue_list.append(node.right)
            # 记录当前层所有节点值
            resl.append(level_list)

        return resl

    def tree_print(self, root: TreeNode, resl=None):
        if resl is None:
            resl = list()

        if root is None:
            return

        # 前序
        resl.append(root.val)
        self.tree_print(root.left, resl)
        # 中序
        # resl.append(root.val)
        self.tree_print(root.right, resl)
        # 后序
        # resl.append(root.val)

        return resl


if __name__ == '__main__':
    root1 = TreeNode("1")
    root1.left = TreeNode("2")
    B = TreeNode("3")
    root1.right = B
    B.left = TreeNode("4")

    print(Solution().level_order(root1))  # [['1'], ['2', '3'], ['4']]
    print(Solution().tree_print(root1))  # ['1', '2', '3', '4']
