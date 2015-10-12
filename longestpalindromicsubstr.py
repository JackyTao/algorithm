# -*- coding: utf-8 -*-


def longest_palindrome(s):
    length_candi = 1

    i = 0
    while i < len(s) - 1:
        l1 = cal_longest(s, i, i)
        l2 = cal_longest(s, i, i + 1)
        length_candi = max(length_candi, l1, l2)
        i = i + 1

    return length_candi


def cal_longest(s, l, r):
    # Pre-condition:
    #   l == r or l == r - 1
    #   the index: l, r must valid in s
    #
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l = l - 1
        r = r + 1
    return r - l - 1


if __name__ == '__main__':
    print longest_palindrome('a')
    print longest_palindrome('ba')
    print longest_palindrome('aba')
    print longest_palindrome('abab')
    print longest_palindrome('ababa')
