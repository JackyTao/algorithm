# -*- coding: utf-8 -*-


def maxarea(heights):
    i, j = 0, len(heights) - 1
    candidate = 0

    while i < j:
        tmp = abs(i - j) * min(heights[i], heights[j])
        candidate = tmp if tmp > candidate else candidate
        if heights[i] > heights[j]:
            j = j - 1
        else:
            i = i + 1

    return candidate


if __name__ == '__main__':
    print maxarea([1, 2, 3, 4])
