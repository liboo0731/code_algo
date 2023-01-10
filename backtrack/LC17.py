from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            if index == len(digits):
                res.append("".join(path.copy()))
                return

            for x in phone_dict[digits[index]]:
                # if x in path:
                #     continue
                path.append(x)
                backtrack(index + 1)
                path.pop()

        res = list()
        path = list()
        backtrack(0)

        return res


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
