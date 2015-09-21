# -*- coding: utf-8 -*-

import sys

a = sys.argv[1].decode('utf-8').encode('gbk')

b = str(', '.join([repr(i) for i in a]))

print b
#print b.replace('\\', '0').strip('[\'').strip('\']')

