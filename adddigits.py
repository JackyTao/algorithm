# -*- coding: utf-8 -*-

def add_digits(num):
    if num < 0:
        return
    rst = 0
    while num > 0:
        rst = num % 10 + rst

        # little tricky here, sum of 2 single digit must be [0, 18]
        # the recursive result actually be: `value - 9`
        rst = rst - 9 if rst >= 10 else rst

        num = num / 10
    return rst

if __name__ == '__main__':
    print 12, add_digits(12)
    print 123, add_digits(123)
    print 1234, add_digits(1234)
    print 12345, add_digits(12345)
    print 123456, add_digits(123456)
