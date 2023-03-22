class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 直接查找第一个匹配项，不存在返回-1
        # return haystack.find(needle)

        # 直接查找第一个匹配项，不存在捕获异常
        # try:
        #     return haystack.index(needle)
        # except ValueError:
        #     return -1

        haystack_len = len(haystack)
        needle_len = len(needle)
        if haystack == needle:
            return 0
        # 子串不存在目标中
        if needle not in haystack:
            return -1

        # 存在子串的前提下，以子串做分割，第一项长度即为所求
        # return len(haystack.split(needle)[0])

        needle_start = needle[0]
        i = haystack.index(needle_start)

        while i < haystack_len - needle_len:
            if haystack[i:i + needle_len] == needle:
                return i
            i += 1

        return i
