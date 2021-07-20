# taken from https://random-matrix-learning.github.io
import numpy as np
import matplotlib.pyplot as plt

n = 100
A = np.random.randn(n,n)
GOE = (A+A.T)/np.sqrt(2*n)

eig = np.linalg.eigvals(GOE)
plt.hist(eig)

# But as we increase dimenstion we get a clearer picture of 
# semicircle

n = 1000
A = np.random.randn(n,n)
GOE = (A+A.T)/np.sqrt(2*n)

eig = np.linalg.eigvals(GOE)
plt.hist(eig)

# And finally 

n = 5000
A = np.random.randn(n,n)
GOE = (A+A.T)/np.sqrt(2*n)

eig = np.linalg.eigvals(GOE)
plt.hist(eig)
