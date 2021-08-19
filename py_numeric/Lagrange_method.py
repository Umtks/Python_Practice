import numpy as np
import matplotlib.pyplot as plt

x = np.array([20, 21, 23, 24, 25, 27, 29, 30],float)
y = np.array([346, 362, 343, 339, 347, 346, 339, 394],float)

def langrange (xp,yp):
  for xi,yi in zip(x,y):
      yp += yi * np.prod((xp - x[x != xi])/(xi - x[x != xi]))
  return yp

xplt = np.linspace(x[0],x[-1])
yplt = np.array([],float)

for xp in xplt:
  yp = langrange(xp,0)
  yplt=np.append(yplt,yp)

x_pred = langrange(26,0)

plt.plot(x, y, "ro", xplt, yplt, "b-")
plt.show()

print(x_pred)