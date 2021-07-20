# taken from https://random-matrix-learning.github.io
import numpy as np
import matplotlib.pyplot as plt

A = np.random.randn(n,n)
GOE = (A+A.T)/np.sqrt(2*n)

eig = np.linalg.eigvals(GOE)
plt.hist(GOE)
