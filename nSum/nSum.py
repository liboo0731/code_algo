def n_sum_val(nums, count, start, target):
    res = list()
    nums_len = len(nums)

    if count < 2 or nums_len < count:
        return res

    if count == 2:
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
    else:
        left = start
        while left < nums_len:
            tmp_list = n_sum_val(nums, count - 1, left + 1, target - nums[left])
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
    n.sort()
    print(n_sum_val(n, 4, 0, 9))
