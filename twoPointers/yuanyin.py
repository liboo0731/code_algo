# 最长的指定瑕疵度的元音子串
def func():
    # 瑕疵数量
    flaw = 1
    input_str = "asdbuiodevauufgh"
    # 元音列表
    yuan_str = "aeiouAEIOU"
    # 找到第一个元音开头的位置
    left = 0
    for x in input_str:
        if x in yuan_str:
            break
        left += 1
    # 使用快慢指针
    right = left
    len_input_str = len(input_str)
    # 设置当前瑕疵度，用于和目标比较
    curr_flaw = 0
    res = ""
    while right < len_input_str:
        if input_str[right] not in yuan_str:
            curr_flaw += 1
        # 当前瑕疵度等于目标，并且两头都是元音字符，则满足要求
        if curr_flaw == flaw and input_str[left] in yuan_str and input_str[right] in yuan_str:
            # 记录最长子串
            res = max(res, input_str[left: right + 1], key=len)
        # 当瑕疵度大于目标时，开始移动左指针，收缩窗口
        while curr_flaw > flaw:
            # 当前不是元音字符时，缩减当前瑕疵度，直到小于等于目标值
            if input_str[left] not in yuan_str:
                curr_flaw -= 1
            left += 1
        # 右指针始终向前
        right += 1
    return res


if __name__ == '__main__':
    print(func())
