# -*- coding: utf-8 -*-


class Mark():
    def __init__(self):
        self.mark = {}

    def get(self, i, j):
        return self.mark.get(i, {}).get(j, None)

    def set(self, i, j, k):
        return self.mark.setdefault(i, {}).setdefault(j, k)


mark = Mark() 

def distance(stra, strb):
    # fetch from cache
    cachev = mark.get(len(stra), len(strb))
    if cachev is not None:
        return cachev
    #
    # real calculate 
    if 0 == len(stra) or 0 == len(strb):
        rst = max(len(stra), len(strb))
    else:
        if stra[-1] == strb[-1]:
            candidate1 = distance(stra[:-1], strb[:-1])
        else:
            candidate1 = distance(stra[:-1], strb[:-1]) + 1
        candidate2 = distance(stra, strb[:-1]) + 1
        candidate3 = distance(stra[:-1], strb) + 1

        rst = min(candidate1, candidate2, candidate3)

    # cache and return
    mark.set(len(stra), len(strb), rst)
    return rst


if __name__ == '__main__':
    mark = Mark()
    print distance('aa', '')
    mark = Mark()
    print distance('abc', 'efg')
    mark = Mark()
    print distance('abc', 'abd')
    mark = Mark()
    print distance('abadbbbbbdfdff', 'abadbbbbbdgdff')
