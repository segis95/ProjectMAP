# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 23:15:53 2016

@author: Sergey
"""

import numpy as np
import matplotlib.pyplot as plt

origin = 'lower'


delta = 0.025

x1 = np.arange(-3.0, 1.5, delta)
y1 = np.arange(-0.05, 9, delta)
X, Y = np.meshgrid(x1, y1)

Z = (X - 1)**2 + 100*(X**2 - Y)**2


CS2 = plt.contour(X, Y, Z, [50 * i for i in range(500)],
                  origin=origin,
                  hold='on')

plt.title('ro = 0.0045')
plt.xlabel('U_1')
plt.ylabel('U_2')


cbar = plt.colorbar(CS2)
cbar.ax.set_ylabel('verbosity coefficient')

cbar.add_lines(CS2)


#*******************GRADIENT DESCENT*****************
x = 1.0
y = 0.0
ro = 0.0045
plt.plot([1.0],[0.0],c = 'black', marker = 'o', markersize=10)
i = 0
#(1.0,0.0)
ax = plt.gca()
while((x - 1.0)**2 + 100.0 * (x**2 - y)**2 > 1e-3):
   x = x - ro * (2 * (x - 1) + 400 * (x**3 - x * y))
   y = y - ro * (100 * (y - x**2))
   i = i + 1
   print(x,y)
   if (i == 1):
       ax.quiver([1.0],[0.0],[-0.45],[1.0],angles='xy',scale = 0.94)
       print(x,y)
   #if (i % 100 == 0):

   plt.plot(x, y, c = 'r', marker = 'o', markersize=2)
   
s = set()
s.add((1,2))   
print(x, y)
                       
plt.savefig('LevelMapOPT3.png')

plt.show()
