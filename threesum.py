# -*- coding: utf-8 -*-


def threesum(a, target):
    # a is already sorted
    if len(a) <= 2:
        return 0, 0, 0
    i = 0
    while i < len(a) - 2:
        j, k = i + 1, len(a) - 1
        while j < k:
            if a[i] + a[j] + a[k] == target:
                return i, j, k
            elif a[i] + a[j] + a[k] > target:
                k = k - 1
            else:
                j = j + 1
        i = i + 1
    return 0, 0, 0


if __name__ == '__main__':
    print threesum([1, 2, 3, 4], 8)
    print threesum([1, 2, 3, 4], 4)
