import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = np.triu(A)

    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print str(i).zfill(3),
        print(x)

    return x

#Going to have to read in A, b, x from file probably. CSV separated maybe?
A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]

n = 20 # number of iterations, might have to work this out myself depending on tolerance level
	   # hopefully not tho...

print gauss(A, b, x, n)
print solve(A, b)