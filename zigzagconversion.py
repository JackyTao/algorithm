# -*- coding: utf-8 -*-


def zigzag(text, k):
    if k == 1:
        return text

    rst = []
    i = 0
    while i < k:
        j = 0
        while True:
            li = 2 * j * (k - 1) - i
            ri = 2 * j * (k - 1) + i
            if i < k - 1:
                if li >= 0 and li < len(text):
                    rst.append(text[li])
                if li >= len(text):
                    break
            if i > 0:
                if ri < len(text):
                    rst.append(text[ri])
                else:
                    break
            j = j + 1
        i = i + 1

    return ''.join(rst)


if __name__ == '__main__':
    print zigzag('paypalishiring', 3)
