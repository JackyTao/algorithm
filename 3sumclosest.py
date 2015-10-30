# -*- coding: utf-8 -*-


def threesumclosest(nums, target):
    nums = sorted(nums)
    delta, candi = None, 0

    i = 0
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1

        while j < k:
            tmp_sum = nums[i] + nums[j] + nums[k]
            if delta is None or delta < abs(tmp_sum - target):
                delta = abs(tmp_sum - target)
                candi = tmp_sum

            if tmp_sum < target:
                j = j + 1
            elif tmp_sum > target:
                k = k - 1
            else:
                return candi
        i = i + 1
        return candi


if __name__ == '__main__':
    print threesumclosest([-1, 2, 1, -4], 1)
