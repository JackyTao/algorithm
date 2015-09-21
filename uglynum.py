# -*- coding: utf-8 -*-

def isugly(n):
    # Positive number which factors only contain 2, 3, 5
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 3 == 0:
            n = n / 3
        elif n % 5 == 0:
            n = n / 5
        else:
            return False
    return True


if __name__ == '__main__':
    print isugly(6)
    print isugly(8)
    print isugly(14)
