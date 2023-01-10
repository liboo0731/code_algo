class Solution:
    @staticmethod
    def area_of_island(grids):
        len_row = len(grids)
        len_col = len(grids[0])

        def dfs(row, col):
            if row < 0 or row == len_row or col < 0 or col == len_col or grids[row][col] != 1:
                return
            # “陆地”变成“海洋”
            grids[row][col] = 2
            for i, j in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                dfs(i, j)

        for x in range(len_row):
            dfs(x, 0)
            dfs(x, len_col - 1)
        # 行列交叉项无需重复遍历
        for y in range(1, len_col - 1):
            dfs(0, y)
            dfs(len_row - 1, y)

        return grids

    @staticmethod
    def max_area_of_island(grids):
        len_row = len(grids)
        len_col = len(grids[0])

        def dfs(row, col):
            if row < 0 or row == len_row or col < 0 or col == len_col or grids[row][col] == 0:
                return 0
            # 搜索过的置为0
            grids[row][col] = 0
            # 当前位置面积加上四周有效面积
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        res = 0
        for x, l in enumerate(grids):
            for y, _ in enumerate(l):
                if grids[x][y] == 1:
                    res = max(res, dfs(x, y))

        return res


if __name__ == '__main__':
    grids1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    import numpy as np
    print(np.array(grids1).shape)
    g = Solution().area_of_island(grids1)
    print(np.array(g))
    print(Solution.max_area_of_island(grids1))

