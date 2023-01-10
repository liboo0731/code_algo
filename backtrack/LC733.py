import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        if curr_color == color:
            return image

        m = len(image)
        n = len(image[0])
        que = collections.deque([(sr, sc)])
        image[sr][sc] = color
        while que:
            x, y = que.popleft()
            # 搜索四个方向
            for r, c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                # 将满足条件的加入队列，采用先进先出原则，将所有满足条件的四周找完
                if 0 <= r <= m - 1 and 0 <= c <= n - 1 and image[r][c] == curr_color:
                    que.append((r, c))
                    image[r][c] = color

        return image


if __name__ == '__main__':
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr = 1
    # sc = 1
    # newColor = 2
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    print(Solution().floodFill(image, sr, sc, newColor))
