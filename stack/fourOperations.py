# 四则运算

def four_operations():
    input_str = input().strip()
    stack = list()
    num = "0"
    oper = "+"

    for i, x in enumerate(input_str):
        if x.isdigit():
            num += x
        if x in ("+", "-", "*", "/") or i == len(input_str) - 1:
            if oper == "+":
                stack.append(int(num))
            elif oper == "-":
                stack.append(-int(num))
            elif oper == "*":
                stack.append(stack.pop() * int(num))
            else:
                if num == "0":
                    return False, 0
                stack.append(stack.pop() / int(num))
            num = ""
            oper = x

    return True, int(sum(stack))


if __name__ == '__main__':
    print(four_operations())
