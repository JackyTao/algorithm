# -*- coding: utf-8 -*-


def reverse(x):
    lead = 1 if x >= 0 else -1
    abspart = abs(x)
    tmppart = 0

    while abspart > 0:
        tmppart = tmppart * 10 + abspart % 10
        abspart = abspart / 10

    return lead * tmppart


if __name__ == '__main__':
    print reverse(123)
    print reverse(-123)
    pass
