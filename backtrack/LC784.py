from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def backtrack(start, char_list):
            result.append("".join(char_list))

            for i in range(start, len(s)):
                if s[i].isdigit():
                    continue
                char_list[i] = char_list[i].swapcase()
                backtrack(i + 1, char_list)
                char_list[i] = char_list[i].swapcase()
                print(char_list)

        result = list()
        s_list = list(s)
        backtrack(0, s_list)

        return result


if __name__ == '__main__':
    print(Solution().letterCasePermutation("a1b2"))
