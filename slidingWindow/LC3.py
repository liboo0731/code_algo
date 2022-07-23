# 3. 无重复字符的最长子串
from collections import defaultdict


def longest_substring(s):
    s_len = len(s)
    # 初始化一个value默认为0的dict
    window = defaultdict(int)

    left = 0
    right = 0
    # 记录最小子串的起始索引及长度
    min_len = float("-inf")

    while right < s_len:
        # 将移入窗口的字符
        char_r = s[right]
        # 扩大窗口
        right += 1
        # 进行窗口内数据更新
        window[char_r] += 1

        # debug 位置
        # print(s[left:right])

        # 判断左窗口是否要收缩
        while window[char_r] > 1:
            min_len = max(min_len, len(window))
            # 将要移出窗口的字符
            char_l = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据更新
            window[char_l] -= 1

    return min_len


if __name__ == '__main__':
    s = "abcbabcbb"
    print(longest_substring(s))
