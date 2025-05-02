from py_ecc.bn128 import (
    G1,
    G2,
    add,
    multiply,
    neg,
    pairing
)

x1, x2, x3 = 5, 7, 9

alpha1 = multiply(G1, 5)  
beta2  = multiply(G2, 6) 
gamma2 = multiply(G2, 3) 
delta2 = multiply(G2, 4)

A1 = multiply(G1, 2)
B2 = multiply(G2, 7)
C1 = multiply(G1, 11)

X1 = add(add(multiply(G1, x1), multiply(G1, x2)), multiply(G1, x3))

pairs = [
    (neg(A1), B2),
    (alpha1, beta2),
    (X1, gamma2),
    (C1, delta2)
]

result = pairing(pairs)

print(result)