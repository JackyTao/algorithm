# -*- coding: utf-8 -*-


def median(A, B):
    # Mid if even, else floor element
    l = len(A) + len(B)
    if l % 2 == 0:
        return (findkth(A, B, (l - 1) / 2) + findkth(A, B, (l + 1) / 2)) / 2.0
    else:
        return findkth(A, B, (len(A) + len(B) - 1) / 2)


def findkth(A, B, k):
    # k: start from 0, so it's k+1th element
    if len(A) > len(B):
        A, B = B, A
    if not A:
        return B[k]
    if len(A) + len(B) - 1 == k:
        return max(A[-1], B[-1])

    # A[0]..A[i] and B[0]..B[j], k + 1 elements in total
    i = len(A) / 2
    j = k - i
    if A[i] > B[j]:
        # A[i] > A[0]..A[i - 1], B[0]..B[j],
        # which means A[i] greater than k + 1 elements already
        # A[i] and elements right are not valid
        # &
        # if B[0]..B[j - 1] is valid, then A[i]..right side someone must be
        # less than B[j], controvsy to above
        return findkth(A[:i], B[j:], i)
    else:
        return findkth(A[i:], B[:j], j)


if __name__ == '__main__':
    pass
