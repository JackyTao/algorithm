# -*- coding: utf-8 -*-


def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) / 2
        if nums[left] <= nums[mid] <= nums[right]:
            right = mid
        elif nums[right] <= nums[left] <= nums[mid]:
            left = mid if left != mid else mid + 1
        elif nums[mid] <= nums[right] <= nums[left]:
            right = mid
        elif nums[left] >= nums[mid] >= nums[right]:
            left = mid if left != mid else mid + 1
        elif nums[right] >= nums[left] >= nums[mid]:
            right = mid
        elif nums[mid] >= nums[right] >= nums[left]:
            left = mid if left != mid else mid + 1
    return left, right


if __name__ == '__main__':
    print find_min([4, 5, 6, 0, 1, 2])
    print find_min([2, 1, 0, 6, 5, 4])
