# -*- coding: utf-8 -*-


def contain_duplicate(nums):
    sorted_nums = sorted(nums)
    i, l = 0, len(sorted_nums)
    while i < l - 1:
        if sorted_nums[i] == sorted_nums[i + 1]:
            return True
        i = i + 1
    return False


def contain_duplicate_m2(nums, k):
    # Distance maximum is k
    tmp_dict = {}
    for i, n in enumerate(nums):
        if n in tmp_dict and abs(i - tmp_dict[n]) <= k:
            return True
        else:
            tmp_dict[n] = i
    return False


if __name__ == '__main__':
    print contain_duplicate([1, 2, 2, 3])
    print contain_duplicate_m2([1, 2, 4, 2, 3], 1)
    print contain_duplicate([1, 2, 3])
    print contain_duplicate_m2([1, 2, 3], 1)
