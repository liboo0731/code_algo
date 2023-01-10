from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, start):
            res.append(path.copy())

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        nums.sort()
        n = len(nums)
        res = []
        backtrack([], 0)

        return res


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
