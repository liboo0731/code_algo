from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i, num in enumerate(nums):
                if check[i]:
                    continue
                if i > 0 and num == nums[i-1] and not check[i-1]:
                    continue
                check[i] = True
                path.append(num)
                backtrack(path)
                check[i] = False
                path.pop()

        nums.sort()
        check = [False for _ in range(len(nums))]
        backtrack([])

        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
