#!/usr/bin/env python3

import sys
import re

decode_pl = { '¡' : 'ą',
              '¢' : 'ć',
              '¦' : 'ę',
              'ª' : 'ł',
              '«' : 'ń',
              '±' : 'ś',
              '»' : 'ż',
              '¹' : 'ź',

for line in sys.stdin:
    line_l = list(line)

    print( re.sub(' +', ' ',''.join( map(lambda x : x if x not in decode_pl else decode_pl[x], line_l))) , end='')
