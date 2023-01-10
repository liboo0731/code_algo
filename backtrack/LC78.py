from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, start):
            res.append(path.copy())

            for i in range(start, n):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        n = len(nums)
        res = []
        backtrack([], 0)

        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
