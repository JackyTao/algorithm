# -*- coding: utf-8 -*-


def traprain(heights):
    base, water = 0, 0
    i, j = 0, len(heights) - 1

    while i < j:
        base_candidate = min(heights[i], heights[j])
        if base_candidate > base:
            water = water + (j - i) * (base_candidate - base)
            base = base_candidate
        if heights[i] > heights[j]:
            j = j - 1
        else:
            i = i + 1

    return water


if __name__ == '__main__':
    print traprain([1, 0, 0, 1])
    print traprain([1, 2, 3, 1])
