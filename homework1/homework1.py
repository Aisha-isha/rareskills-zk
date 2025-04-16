# Problem4

p = 71
A = [
    [1,1],
    [1,4]
    ]

det = 3
modular_det= pow (3,-1,p)
print("Modular inverse of deterninant is ", modular_det)

A_inverse= [
    [4*modular_det%p ,-1*modular_det%p],
    [-1*modular_det%p ,1*modular_det%p]
]

print("Inverse A ")
for row in A_inverse:
    print(row)

result = [
    [(A[0][0] * A_inverse[0][0] + A[0][1] * A_inverse[1][0]) % p,
     (A[0][0] * A_inverse[0][1] + A[0][1] * A_inverse[1][1]) % p],
    [(A[1][0] * A_inverse[0][0] + A[1][1] * A_inverse[1][0]) % p,
     (A[1][0] * A_inverse[0][1] + A[1][1] * A_inverse[1][1]) % p]
]

print("AA-1 ")
for row in result:
    print(row)

# Problem 5

print("The modular square root of 12")
for i in range(p):
    if (i*i)%p == 12:
        print(i)