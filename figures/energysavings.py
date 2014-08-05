#!/usr/bin/env python

import numpy as np
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'], 'size': 8})
rc('text', usetex=True)

import matplotlib.pyplot as plt

two_chunks = [2.64261299175,
    5.7676196625,
    7.913916384,
    10.71312763,
    14.0002759505,
    17.236713588,
    20.578611456,
    21.633931746,
    24.84951772825,
    28.6106781825,
    32.54724684,
    36.10363393,
    40.5136778975,
    40.478871054,
    43.69182402375,
    51.207808007,
    50.80598575,
    51.4820978685,
    55.9379803775,
    60.74259834825
    ]

one_chunk = [0.932766152,
    2.472025944,
    3.310061995,
    5.168117376,
    7.690023538,
    10.28697088,
    8.580135572,
    10.274920498,
    10.532629494,
    3.472664896,
    16.522250544,
    26.88835584,
    18.92447436,
    21.212547552,
    22.02619176,
    21.572091685,
    23.757437152,
    27.429719527,
    26.977785876,
    20.284497716]


N = 20

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, one_chunk, width, color='b', label='\\textbf{One chunk}')
rects2 = ax.bar(ind+width, two_chunks, width, color='g', label='\\textbf{Two chunks}')
'''rects3 = ax.bar(ind+2*width, [(t / 1000.) for t in wan_download], width, color='r', label='\\textbf{WAN Wifi}')
rects4 = ax.bar(ind+3*width, [(t / 1000.) for t in orch_arranged], width, color='c', label='\\textbf{Arranged Wifi}')
rects4 = ax.bar(ind+3*width, [(t / 1000.) for t in orch_arranged], width,
    color='y', label='\\textbf{LTE}')'''


ax.set_ylabel('\\textbf{Energy Consumption (J)}')
ax.set_xlabel('\\textbf{File Size (Mb)}')

ax.set_xticks(ind+width)

ax.set_xticklabels([str(l) for l in np.arange(5, 105, 5)])

ax.legend(loc ='upper left', fontsize=8)

fig.set_size_inches(3.5, 2.5)

plt.savefig('energysavings.pdf', bbox_inches='tight')
