# 76. 最小覆盖子串
from collections import defaultdict


def min_window(s, t):
    s_len = len(s)
    # 初始化一个value默认为0的dict
    # window = defaultdict(lambda: 0)
    window = defaultdict(int)
    # 所有有效字符计数
    need = defaultdict(int)
    for x in t:
        need[x] += 1
    need_len = len(need)

    left = 0
    right = 0
    valid = 0
    # 记录最小子串的起始索引及长度
    start = 0
    sub_len = float("inf")

    while right < s_len:
        # 将移入窗口的字符
        char_r = s[right]
        # 扩大窗口
        right += 1
        # 进行窗口内数据更新
        if char_r in need:
            window[char_r] += 1
            if need[char_r] == window[char_r]:
                valid += 1

        # debug位置
        # print(s[left:right])

        # 判断左窗口是否要收缩
        while valid == need_len:
            # 在这里更新最小覆盖子串
            if right - left < sub_len:
                start = left
                sub_len = right - left
            # 将要移出窗口的字符
            char_l = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据更新
            if char_l in need:
                if window[char_l] == need[char_l]:
                    valid -= 1
                window[char_l] -= 1

    return "" if sub_len == float("inf") else s[start: start + sub_len]


if __name__ == '__main__':
    s = "CBADOBECODEBANCB"
    t = "ABC"
    print(min_window(s, t))
