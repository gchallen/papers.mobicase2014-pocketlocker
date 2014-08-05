#!/usr/bin/env python

import numpy as np
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'], 'size': 8})
rc('text', usetex=True)

import matplotlib.pyplot as plt

econly = [480.6666666667,
    947,
    1198.3333333333,
    1586.6666666667,
    2027.3333333333,
    2979.3333333333,
    3292.3333333333,
    3821.6666666667,
    4365.3333333333,
    4786.3333333333,
    4964,
    5424,
    6117.3333333333,
    6649.3333333333,
    7245,
    7665.6666666667,
    8281.6666666667,
    8538.3333333333,
    8348.6666666667,
    8026.3333333333
    ]


local_lan = [4202.3333333333,
    6600,
    9698.3333333333,
    14685,
    19847.3333333333,
    26567,
    31970.3333333333,
    27249.3333333333,
    29828,
    38784.3333333333,
    36011.6666666667,
    37618,
    41649.3333333333,
    48451.3333333333,
    46013.3333333333,
    49356.6666666667,
    57010.6666666667,
    52993.6666666667,
    58502.6666666667,
    66093
    ]

wan_download = [5962.3333333333,
    11668.6666666667,
    17501.6666666667,
    23282,
    28807.3333333333,
    35067,
    40080.6666666667,
    46208.6666666667,
    51915.6666666667,
    58033,
    63278.6666666667,
    69279.3333333333,
    74698.3333333333,
    81212,
    85791,
    92090,
    97835,
    104029,
    109197.666666667,
    115983
    ]


orch_arranged = [11467.3333333333,
    20859.6666666667,
    31218.3333333333,
    39053,
    49006,
    60984,
    74963.3333333333,
    84140,
    93240.6666666667,
    107465.333333333,
    109502.333333333,
    131018,
    142464,
    158052.666666667,
    155239.666666667,
    175516.666666667,
    177467,
    193411.666666667,
    196601,
    226773.333333333
    ]

lte = [
25.28,
26.52,
37.19,
47.16,
59.31,
71.95,
85.57,
92.37,
114.49,
114.25,
113.52,
132.97,
142.93,
161.41,
148.53,
152.9,
185.23,
196.9,
205.6,
217.81
]


N = 20

ind = np.arange(N)  # the x locations for the groups
width = 0.16       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, [(t / 1000.) for t in econly], width, color='b', label='\\textbf{On Device}')
rects2 = ax.bar(ind+width, [(t / 1000.) for t in local_lan], width, color='g', label='\\textbf{LAN Wifi}')
rects3 = ax.bar(ind+2*width, [(t / 1000.) for t in wan_download], width, color='r', label='\\textbf{WAN Wifi}')
rects4 = ax.bar(ind+3*width, [(t / 1000.) for t in orch_arranged], width, color='c', label='\\textbf{Arranged Wifi}')
rects4 = ax.bar(ind+4*width, [(t) for t in lte], width, color='y', label='\\textbf{LTE}')

ax.set_ylabel('\\textbf{File Access Time (s)}')
ax.set_xlabel('\\textbf{File Size (Mb)}')

ax.set_xticks(ind+width)

ax.set_xticklabels([str(l) for l in np.arange(5, 105, 5)])

ax.legend(loc ='upper left', fontsize=8)

fig.set_size_inches(6.5, 2.5)

plt.savefig('downloadtimes.pdf', bbox_inches='tight')
