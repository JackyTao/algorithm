# -*- coding: utf-8 -*-


def traprain(heights):
    # Sticks with no width
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


def traprain2(heights):
    # Sticks with width
    water = 0
    i, j = 0, len(heights) - 1

    while i < j - 1:
        if heights[i] > heights[j]:
            if heights[j] > heights[j - 1]:
                water = water + heights[j] - heights[j - 1]
                heights[j - 1] = heights[j]
            j = j - 1
        else:
            if heights[i] > heights[i + 1]:
                water = water + heights[i] - heights[i + 1]
                heights[i + 1] = heights[i]
            i = i + 1
    return water


def traprain22(heights):
    # Sticks with width
    # without changing the input array
    if len(heights) <= 2:
        return 0

    i, j = 0, len(heights) - 1
    water = 0
    baseL, baseR = heights[i], heights[j]

    while i < j - 1:
        if baseL > baseR:
            if baseR > heights[j - 1]:
                water = water + baseR - heights[j - 1]
            else:
                baseR = heights[j - 1]
            j = j - 1
        else:
            if baseL > heights[i + 1]:
                water = water + baseL - heights[i + 1]
            else:
                baseL = heights[i + 1]
            i = i + 1
    return water


if __name__ == '__main__':
    print traprain([1, 2, 3, 1])
    print traprain([1, 0, 0, 1])
    print traprain2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
