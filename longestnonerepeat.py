# -*- coding: utf-8 -*-


def longest(s):
    # similar to: `move zeros`, `two sum`, etc.
    # literaly O(n^2)
    # O(n) exists
    i, j = -1, 0
    keys = set()
    candidate = 0

    while j < len(s):
        # In every round, calculate `the longest which s[j] as the tail`
        while s[j] in keys:
            if i >= 0:
                keys.remove(s[i])
            i = i + 1
        keys.add(s[j])
        candidate = len(keys) if len(keys) > candidate else candidate
        j = j + 1

    return candidate


if __name__ == '__main__':
    print longest('aaaa')
    print longest('a')
    print longest('abcdef')
    print longest('abab')
    print longest('')
