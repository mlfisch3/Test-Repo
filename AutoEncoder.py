import numpy as np

Nh = 5
Nx = 10
Wxy = np.random.randn(Nh, Nx)
by = np.random.randn(Nh)
WhX = np.random.randn(Nx, Nh)
bX = np.random.randn(Nx)
x = np.ones(Nx)
y = np.matmul(Wxy, x) + by
print(y)

import requests

r = requests.