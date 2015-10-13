# -*- coding: utf-8 -*-


def threesum(nums):
    nums = sorted(nums)
    i = 0
    result = []
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == 0:
                if [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])

                # To change condition, `accepted` by leetcode 
                j = j + 1
            elif tmp > 0:
                k = k - 1
            else:
                j = j + 1
        i = i + 1

    return result


if __name__ == '__main__':
    print threesum([-1, 0, 1, 2, -1, -4])
