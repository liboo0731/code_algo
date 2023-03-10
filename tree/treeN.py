# 前序，后序遍历
# 层序遍历

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.child_list = list()

    def add_child(self, node):
        self.child_list.append(node)


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
                # 子节点加入队列
                queue_list.extend(node.child_list)
            # 记录当前层所有节点值
            resl.append(level_list)

        return resl

    def pre_order(self, root: TreeNode, resl=None):
        if resl is None:
            resl = list()

        if root is None:
            return

        resl.append(root.val)
        for node in root.child_list:
            self.pre_order(node, resl)

        return resl

    def post_order(self, root: TreeNode, resl=None):
        if resl is None:
            resl = list()

        if root is None:
            return

        for node in root.child_list:
            self.post_order(node, resl)
        resl.append(root.val)

        return resl


if __name__ == '__main__':
    root1 = TreeNode("1")
    root1.add_child(TreeNode("2"))
    B = TreeNode("3")
    root1.add_child(B)
    B.add_child(TreeNode("4"))
    root1.add_child(TreeNode("5"))

    print(Solution().level_order(root1))  # [['1'], ['2', '3', '5'], ['4']]
    print(Solution().pre_order(root1))  # ['1', '2', '3', '4', '5']
    print(Solution().post_order(root1))  # ['2', '4', '3', '5', '1']
