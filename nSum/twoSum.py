def two_sum_val(nums, target):
    # 先排序
    nums.sort()
    res = list()

    left = 0
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


def two_sum_index(nums, target):
    # 获取下标，需要把值与下标绑定后排序
    nums_sort = sorted(enumerate(nums), key=lambda x: x[1])
    res = list()

    left = 0
    right = len(nums_sort) - 1

    while left < right:
        sum_val = nums_sort[left][1] + nums_sort[right][1]
        # 记录左右指针当前值，用于去重
        left_val = nums_sort[left][1]
        right_val = nums_sort[right][1]

        if sum_val > target:
            # 跳过不满足条件的右指针重复项
            while left < right and nums_sort[right][1] == right_val:
                right -= 1
        elif sum_val < target:
            # 跳过不满足条件的左指针重复项
            while left < right and nums_sort[left][1] == left_val:
                left += 1
        else:
            # list index时间复杂度是O(1)
            res.append([nums_sort[left][0], nums_sort[right][0]])
            # 跳过满足条件的左，右指针重复项
            while left < right and nums_sort[left][1] == left_val:
                left += 1
            while left < right and nums_sort[right][1] == right_val:
                right -= 1

    return res


if __name__ == '__main__':
    n = [1, 2, 4, 2, 5, 3]
    t = 4
    print(two_sum_index(n, t))
    print(two_sum_val(n, t))
