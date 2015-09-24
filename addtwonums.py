# -*- coding: utf-8 -*-


def add_two_num(l1, l2):
    # l1: [1, 3, 2] which means: 231
    if len(l1) > len(l2):
        l, s = l1, l2
    else:
        l, s = l2, l1

    pre, i = 0, 0
    while i < len(l):
        cur_digit_sum = l[i] + (s[i] if i < len(s) else 0) + pre

        l[i] = cur_digit_sum % 10
        pre = cur_digit_sum / 10

        i = i + 1
    if pre > 0:
        l.append(1)
    print l


if __name__ == '__main__':
    add_two_num([2, 4, 3], [5, 6, 4])
