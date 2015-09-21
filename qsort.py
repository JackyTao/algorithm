# -*- coding: utf-8 -*-


def qsort(a, left, right):
    # exterminate
    if left >= right:
        return

    # pivot
    m = i = left
    while i <= right:
        if a[i] < a[left]:
            m = m + 1
            a[m], a[i] = a[i], a[m]
        i = i + 1

    a[left], a[m] = a[m], a[left]

    # recursively
    qsort(a, left, m - 1)
    qsort(a, m + 1, right)


if __name__ == '__main__':
    a = [5, 4, 3, 2, 1]
    qsort(a, 0, 4)
    print a
    a = [5, 4]
    qsort(a, 0, 1)
    print a
    a = [5]
    qsort(a, 0, 0)
    print a
    a = [5, 7, 3, 2, 1]
    qsort(a, 0, 4)
    print a
