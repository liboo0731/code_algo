def first_left_val(nums):
    len_nums = len(nums)
    resl = [0] * len_nums
    stack = list()

    for i in range(len_nums):
        if not stack:
            stack.append(nums[i])
            resl[i] = 0
        else:
            # 第一个取0，后面不存在比它小或者大的数取-1
            # 左边第一个最小值
            # while stack and nums[i] < stack[-1]:  # [0, -1, 3, 3, 4, -1]
            # 左边第一个最大值
            while stack and nums[i] > stack[-1]:  # [0, 10, 10, 7, -1, 12]
                stack.pop()
            if stack:
                resl[i] = stack[-1]
            else:
                resl[i] = -1
            stack.append(nums[i])
    return resl


if __name__ == '__main__':
    print(first_left_val([10, 3, 7, 4, 12, 2]))
