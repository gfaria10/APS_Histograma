# -*- coding: utf-8 -*-
"""
Listing 1-1. PLOTTING_AREA
"""

import numpy
import matplotlib

x1=-20
x2=15
y1=-10
y2=10

plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(True)

plt.show()