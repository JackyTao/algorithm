# -*- coding: utf-8 -*-

# Mergetwo files which have the same keys

kuo = {l.split()[0]: int(l.split()[1]) for l in open('co')}
kug = {l.split()[0]: int(l.split()[1]) for l in open('cg')}


ku = set(kuo.keys()) | set(kug.keys())


for k in ku:
    print k, kuo.get(k, 0), kug.get(k, 0)



