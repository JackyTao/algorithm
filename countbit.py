# -*- coding: utf-8 -*-


def countbit(num):
    # Bit operation
    count = 0
    while num > 0:
        num = num & (num - 1)
        count = count + 1

    return count


def countbit2(num):
    # Divide each round
    count = 0
    while num > 0:
        if num % 2 == 1:
            count = count + 1
        num = num / 2
    return count


if __name__ == '__main__':
    print countbit(23), countbit2(23)
    print countbit(4342), countbit2(4342)
