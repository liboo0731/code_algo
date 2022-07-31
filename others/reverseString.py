# 递归的方式反转字符串，理解树的前，后序遍历
def reverse_string(s, i):
    if i == len(s):
        return

    # 前序
    # print(s[i])
    reverse_string(s, i + 1)
    # 后序
    print(s[i])


if __name__ == '__main__':
    s1 = "123456789"
    reverse_string(s1, 0)
