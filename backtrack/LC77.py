from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(path, start):
            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(start, n + 1):
                if (n + 1 - start + len(path)) < k:
                    return
                path.append(i)
                backtrack(path, i + 1)
                path.pop()

        res = []
        backtrack([], 1)

        return res


if __name__ == '__main__':
    print(Solution().combine(4, 3))
