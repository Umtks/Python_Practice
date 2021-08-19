import numpy as np
import matplotlib.pyplot as plt

x = np.array([20, 21, 23, 24, 25, 27, 29, 30])
y = np.array([346, 362, 343, 339, 347, 346, 339, 394])

v = np.vander(x, increasing=True)

coef = np.linalg.solve(v, y)

def direct(coef,p):
    vp = np.vander([p], len(x), increasing=True)
    result = 0
    for i in range(len(coef)):
        result += vp[:,i]*coef[i]
    return result


pred = direct(coef,26)


xplt = np.linspace(x[0],x[-1])
yplt = np.array([],float)

for i in xplt:
    yplt =np.append(yplt,direct(coef,i))

plt.plot(x, y, "ro", xplt, yplt, "b-")
plt.show()
print(pred)