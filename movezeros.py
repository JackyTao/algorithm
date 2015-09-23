# -*- coding: utf-8 -*-


def move_zeros(nums):
    i, end = 0, len(nums) - 1
    while i < end:
        if nums[i] == 0:
            # bubble up
            j = i
            while j < end:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j = j + 1
            nums[end] = 0
            end = end - 1
        i = i + 1
    print nums


def move_zeros_2(nums):
    # similar to qsort
    # m: upper boundary which not equals to 0
    # i: index of ele to check
    m, i, l = -1, 0, len(nums)
    while i < l:
        if nums[i] != 0:
            m = m + 1
            nums[m], nums[i] = nums[i], nums[m]
        i = i + 1
    print nums


if __name__ == '__main__':
    move_zeros([1, 0, 3, 5, 0])
    move_zeros_2([1, 0, 3, 5, 0])
