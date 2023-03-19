class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeOperations:
    def build_tree_pre_mid(self, pre_order: list, mid_order: list):
        if not pre_order:
            return

        # 前序第一个值为根节点
        root = TreeNode(pre_order[0])
        # 中序中找到根节点所在位置，两边分别为左右子树
        mid_index = mid_order.index(root.val)

        root.left = self.build_tree_pre_mid(pre_order[1:mid_index + 1], mid_order[:mid_index])
        root.right = self.build_tree_pre_mid(pre_order[mid_index + 1:], mid_order[mid_index + 1:])

        return root

    def build_tree_lst_mid(self, lst_order: list, mid_order: list):
        if not lst_order:
            return

        # 后序的最后一个值为根节点
        root = TreeNode(lst_order[-1])
        mid_index = mid_order.index(root.val)

        root.left = self.build_tree_lst_mid(lst_order[:mid_index], mid_order[:mid_index])
        root.right = self.build_tree_lst_mid(lst_order[mid_index: -1], mid_order[mid_index + 1:])

        return root

    def print_tree_dfs(self, root: TreeNode, res=None):
        if res is None:
            from collections import defaultdict
            res = defaultdict(list)
        if not root:
            return
        # 前序
        res["pre"].append(root.val)
        self.print_tree_dfs(root.left, res)
        # 中序
        res["mid"].append(root.val)
        self.print_tree_dfs(root.right, res)
        # 后序
        res["lst"].append(root.val)

        return res

    @staticmethod
    def print_tree_bfs(root: TreeNode, res=None):
        if res is None:
            res = list()
        if not root:
            return

        from collections import deque
        dq = deque()
        dq.append(root)

        while dq:
            dp_size = len(dq)
            # 记录当前层节点
            level_list = list()

            for _ in range(dp_size):
                # 不能使用下标来标记节点，因为队列的长度循环一次后就会变化，而range始终按照最开始长度迭代
                node = dq.popleft()
                level_list.append(node.val)
                # res.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            res.append(level_list)

        return res


def func():
    a = TreeNode(1)
    a.left = TreeNode(2)
    b = TreeNode(3)
    a.right = b
    b.left = TreeNode(4)
    b.right = TreeNode(5)

    print(TreeOperations().print_tree_dfs(a))
    pre = [1, 2, 3, 4, 5]
    mid = [2, 1, 4, 3, 5]
    lst = [2, 4, 5, 3, 1]
    print(TreeOperations().print_tree_bfs(a))
    level = [[1], [2, 3], [4, 5]]

    root1 = TreeOperations().build_tree_pre_mid(pre, mid)
    print(TreeOperations().print_tree_dfs(root1))
    root2 = TreeOperations().build_tree_lst_mid(lst, mid)
    print(TreeOperations().print_tree_dfs(root2))


if __name__ == '__main__':
    func()
