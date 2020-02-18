import numpy as np
import matplotlib.pyplot as plt

# integrand function
def intergrand(u, v):
	return v * u / (u**2 + v**2)**(3/2)

# simple integration function
def integrate(a, b, N, f, param):
	dx = (b - a)/N
	
	sum = 0
	
	for i in range(int(N)):
		x = a + dx * i
		sum += f(x, param) * dx
		
	return sum

# integration resolution
N = int(1e3)
# model resolution
M = int(1e2)

# set up arrays for height & field
v_arr = np.linspace(0.001, 10, M)
eta_arr = np.zeros(len(v_arr))

# integrate
for i in range(len(v_arr)):
	eta_arr[i] = integrate(0, 1, N, intergrand, v_arr[i])

# plot result
plt.plot(eta_arr, v_arr)
plt.grid('on')
plt.xlabel("Dimensionless E-field, $E k^{-1} s^{-1}$)")
plt.ylabel("Dimensionless Height above Disk, $z R^{-1}$")
plt.savefig("Height vs Field.png")
plt.show()
