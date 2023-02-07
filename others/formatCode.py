def format_code():
    # 数字代表缩进几次，可以多行缩进
    # input_list = [1, 2, 3, 2, 1]  # 3
    # input_list = [0, 1, 2, 0, 3, 2, 1]  # 2+3=5
    input_list = [0, 1, 2, 1, 3, 2, 1]  # 1+1+2=4
    step = input_list[0]
    len_i = len(input_list)
    # 求得
    for x in range(1, len_i):
        if input_list[x] > input_list[x - 1]:
            step += input_list[x] - input_list[x - 1]

    return step


if __name__ == '__main__':
    print(format_code())
