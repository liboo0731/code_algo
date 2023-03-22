class Solution:
    def func(self):
        # 括号内的字符串反转
        input_str = "(u(love)i)"
        stack = list()
        tmp_str = ""
        for x in input_str:
            if x == "(":
                # 遇到左括号将临时子串入栈，重新开始记录
                stack.append(tmp_str)
                tmp_str = ""
            elif x == ")":
                # 遇到右括号，反转临时子串，并与栈顶元素相加
                tmp_str = stack.pop() + tmp_str[::-1]
            else:
                tmp_str += x

        return tmp_str


if __name__ == '__main__':
    print(Solution().func())
