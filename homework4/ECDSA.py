import hashlib
import secrets
from ecdsa import SECP256k1, ellipticcurve

# courbe secp256k1
curve = SECP256k1.curve
generator = SECP256k1.generator
curve_order = SECP256k1.order

def modinv(k, mod):
    return pow(k, -1, mod)

# 1. generation de private key
private_key = secrets.randbelow(curve_order - 1) + 1
print("Private Key :", hex(private_key), "\n")

# 2. generation de public key
public_key = generator * private_key
print("Public Key Coordinates:")
print("x =", hex(public_key.x()))
print("y =", hex(public_key.y()), "\n")

# 3. pick msg and hash it
message = b"message pour le hash"
hash_bytes = hashlib.sha256(message).digest()
h = int.from_bytes(hash_bytes, 'big')
print("Message hash :", hex(h), "\n")

# 4. sign le message
def sign_message(priv_key, h):
    while True:
        k = secrets.randbelow(curve_order - 1) + 1
        R = generator * k
        r = R.x() % curve_order

        if r == 0:
            continue

        k_inv = modinv(k, curve_order)
        s = (k_inv * (h + r * priv_key)) % curve_order

        if s == 0:
            continue

        return (r, s)
        
signature = sign_message(private_key, h)
r, s = signature
print("ECDSA Signature:")
print("r =", hex(r))
print("s =", hex(s), "\n")

# 5. vérifier la validité de la signature
def verify_signature(pub_key, signature, h):
    r, s = signature
    s_inv = modinv(s, curve_order)
   
    u1 = (h * s_inv) % curve_order
    u2 = (r * s_inv) % curve_order

    point = (generator * u1) + (pub_key * u2)
    
    return (point.x() % curve_order) == r

# vérification de la signature
valid = verify_signature(public_key, signature, h)
if valid:
    print("Valid signature \n")
else : 
    print("invalid signature \n")