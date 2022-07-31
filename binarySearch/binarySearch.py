def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid


def left_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left >= len(nums) or nums[left] != target:
        return -1

    return left


def right_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid + 1

    if right < 0 or nums[right] != target:
        return -1

    return right


if __name__ == '__main__':
    n = [1, 2, 2, 2, 4, 6, 7]
    t = 2
    print(binary_search(n, t))
    print(left_bound(n, t))
    print(right_bound(n, t))
