def two_sum_val(nums, start, target):
    # 先排序
    nums.sort()
    res = list()

    left = start
    right = len(nums) - 1

    while left < right:
        sum_val = nums[left] + nums[right]
        # 记录左右指针当前值，用于去重
        left_val = nums[left]
        right_val = nums[right]

        if sum_val > target:
            # 跳过不满足条件的右指针重复项
            while left < right and nums[right] == right_val:
                right -= 1
        elif sum_val < target:
            # 跳过不满足条件的左指针重复项
            while left < right and nums[left] == left_val:
                left += 1
        else:
            res.append([nums[left], nums[right]])
            # 跳过满足条件的左，右指针重复项
            while left < right and nums[left] == left_val:
                left += 1
            while left < right and nums[right] == right_val:
                right -= 1

    return res


def three_sum_val(nums, start, target):
    nums_len = len(nums)
    # 先排序
    nums.sort()
    res = list()

    left = start
    while left < nums_len:
        tmp_list = two_sum_val(nums, left + 1, target - nums[left])
        for item in tmp_list:
            item.append(nums[left])
            res.append(item)
        # 跳过重复项
        while left < nums_len - 1 and nums[left] == nums[left + 1]:
            left += 1
        left += 1

    return res


def four_sum_val(nums, target):
    nums_len = len(nums)
    # 先排序
    nums.sort()
    res = list()

    left = 0
    while left < nums_len:
        tmp_list = three_sum_val(nums, left + 1, target - nums[left])
        for item in tmp_list:
            item.append(nums[left])
            res.append(item)
        # 跳过重复项
        while left < nums_len - 1 and nums[left] == nums[left + 1]:
            left += 1
        left += 1

    return res


if __name__ == '__main__':
    n = [1, 2, 4, 2, 5, 3]
    t = 9
    print(four_sum_val(n, t))
