class Solution:
    def func(self, s: str):
        dict_count = dict()
        for x in s:
            if x in dict_count:
                dict_count[x] += 1
            else:
                dict_count[x] = 1

        # dict_count_ji = {k: v for k, v in dict_count.items() if v % 2 == 1}
        # count_ji = len(dict_count_ji)
        # 判断是否可以组成回文串时，如果奇数字符的数量大于1，则不行
        # count_ji = len([x for x in dict_count.values() if x % 2 == 1])

        # 记录回文左半边子串
        res_left = ""
        for c, count in sorted(dict_count.items()):
            # 如果要使用所有字符数量，这里只去偶数字符
            # 将数量大于1的字符分配
            res_left += c * (count // 2)
        # 中间放一个数量为奇数的字符
        res_mid = ""
        # 如果要使用所有字符数量，这里去奇数数量最大的直接放中间
        # 逆序，把大的放前边
        for c, count in sorted(dict_count.items(), reverse=True):
            if count % 2 == 1:
                res_mid += c
                break
        res = res_left + res_mid + res_left[::-1]

        return res  # abcefzzfzzfecba


if __name__ == '__main__':
    print(Solution().func("abcabceeezzzzfff"))
