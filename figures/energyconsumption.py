#!/usr/bin/env python

import numpy as np
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'], 'size': 8})
rc('text', usetex=True)

import matplotlib.pyplot as plt

econly = [0.7669098225,
    1.763362835,
    2.544086034,
    3.64247468475,
    4.57265015225,
    5.67759695125,
    7.31252862375,
    8.114625696,
    9.94584298825,
    10.1046121435,
    11.307414378,
    13.0017246865,
    14.0358986625,
    15.99764209425,
    16.526478904,
    17.8067433765,
    19.10053886,
    20.2715558375,
    22.08041784075,
    24.44041845,
    ]


local_lan = [2.64261299175,
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

wan_download = [5.49562184,
    9.90157049333,
    13.7233746167,
    20.8879650767,
    23.3116504467,
    28.06668596,
    29.6148049333,
    35.8995731333,
    35.5837331167,
    40.8060724633,
    41.1219656367,
    48.26150907,
    43.68064711,
    44.8986266767,
    51.50908676,
    51.3790967567,
    58.44318387,
    73.4121108233,
    58.37141608,
    64.3216455733
    ]


orch_arranged = [2.713580592,
    8.403851736,
    13.938542616,
    19.28080383125,
    31.1338147425,
    28.0860809715,
    33.07361928325,
    39.273632832,
    44.48635726925,
    53.1888373095,
    54.335162337,
    57.988256697,
    65.4564447,
    67.73488208375,
    76.52973588,
    88.0874546475,
    83.50611154875,
    96.43797831125,
    97.818510684,
    100.43481465
    ]

lte=[24.3006528,
    26.97821256,
    40.37684829,
    49.02876216,
    83.3240259,
    79.97897245,
    98.30392841,
    105.7091517,
    128.17682154,
    135.05641025,
    131.50531416,
    153.80560118,
    168.16086118,
    183.68006052,
    178.84363623,
    181.0449146,
    215.59771758,
    230.6307421,
    228.0714632,
    247.46679179
    ]


N = 20

ind = np.arange(N)  # the x locations for the groups
width = 0.16       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, [(t) for t in econly], width, color='b', label='\\textbf{On Device}')
rects2 = ax.bar(ind+width, [(t) for t in local_lan], width, color='g', label='\\textbf{LAN Wifi}')
rects3 = ax.bar(ind+2*width, [(t) for t in wan_download], width, color='r', label='\\textbf{WAN Wifi}')
rects4 = ax.bar(ind+3*width, [(t) for t in orch_arranged], width, color='c', label='\\textbf{Arranged Wifi}')
rects4 = ax.bar(ind+4*width, [(t) for t in lte], width,
    color='y', label='\\textbf{LTE}')


ax.set_ylabel('\\textbf{Energy Consumption (J)}')
ax.set_xlabel('\\textbf{File Size (Mb)}')

ax.set_xticks(ind+width)

ax.set_xticklabels([str(l) for l in np.arange(5, 105, 5)])

ax.legend(loc ='upper left', fontsize=8)

fig.set_size_inches(6.5, 2.5)

plt.savefig('energyconsumption.pdf', bbox_inches='tight')
