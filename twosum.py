# -*- coding: utf-8 -*-


def twosum(a, target):
    if len(a) < 2:
        return
    i, j = 0, len(a) - 1
    while i < j:
        print i, j
        candi = a[i] + a[j]
        if candi == target:
            return [i + 1, j + 1]
        elif candi < target:
            i = i + 1
        else:
            j = j - 1


if __name__ == '__main__':
    print twosum([2, 7, 11, 15], 9)
