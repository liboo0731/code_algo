from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path, start):
            if sum(path) == target:
                res.append(path.copy())

            for i in range(start, len(candidates)):
                if sum(path) > target:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path, i + 1)
                path.pop()

        candidates.sort()
        res = []
        backtrack([], 0)

        return res


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
