# -*- coding: utf-8 -*-

f = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
     'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Forteen', 'Fifteen', 'Sixteen',
     'Seventeen', 'Eighteen', 'Ninteen']
s = [
    'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
    'Sixty', 'Seventy', 'Eighty', 'Ninty'
]


def int2words(num):
    q = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
    p = 0

    while num > 0:
        remain = num % 1000
        num = num / 1000


def small2words(num):
    # int less than 1000
    rst = ['', '', '']
    p1 = num / 100
    p2 = (num % 100) / 10
    p3 = num % 10

    if p1 > 0:
        rst[0] = f[p
