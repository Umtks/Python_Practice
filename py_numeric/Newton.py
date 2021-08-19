import numpy as np
import matplotlib.pyplot as plt

x = np.array([20, 21, 23, 24, 25, 27, 29, 30])
y = np.array([346, 362, 343, 339, 347, 346, 339, 394])

def NNDcoeffs(x, y):
  n = np.shape(y)[0]
  pyramid = np.zeros([n,n])
  pyramid[::,0] = y
  for i in range(1,n):
    for j in range(n-i):
      pyramid[j][i] = (pyramid[j+1][i-1] - pyramid[j][i-1]) / (x[j+i] - x[j])
  return pyramid[0]

coeff_vector = NNDcoeffs(x, y)

final_pol = np.polynomial.Polynomial([0.])
n = coeff_vector.shape[0]

for i in range(n):
  p = np.polynomial.Polynomial([1.])
  for j in range(i):
    p_temp = np.polynomial.Polynomial([-x[j], 1.])
    p = np.polymul(p, p_temp)
  p *= coeff_vector[i]
  final_pol = np.polyadd(final_pol, p)

p = np.flip(final_pol[0].coef, axis=0)

x_axis = np.linspace(20, 30, num=5000)
y_axis = np.polyval(p, x_axis)

plt.plot(x, y, "ro", x_axis, y_axis, "b-")
plt.show()

print(np.polyval(p,26))