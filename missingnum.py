# -*- coding: utf-8 -*-

def missingnum(a=None):
    if not a:
        return
    full = len(a) * (len(a) + 1) / 2
    return full - sum(a)


if __name__ == '__main__':
    print missingnum([0, 1, 2])
