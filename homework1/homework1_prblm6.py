import galois

pe=71
GF = galois.GF(pe)

p = galois.Poly([52, 24, 61], field=GF)
q = galois.Poly([40, 40, 58], field=GF)

sum_poly = p + q
prod_poly = p * q

roots_p = p.roots()
roots_q = q.roots()
roots_prod = prod_poly.roots()

print("p(x)+q(x) = ", sum_poly)
print("p(x)*q(x):", prod_poly)
print("p(x) roots : ", roots_p)
print("q(x) roots :", roots_q)
print("Product roots", roots_prod)