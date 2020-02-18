ABC = "abcdefghijklmnopqrstuvwxyz"

def encrypt(a, b, msg):
    """Encrypt a message with the affine cypher.

    Use `a` as the multiplicative constant and `b` as the additive constant.
    If `a` == 1 this reduces to the Caesar cipher.
    If `a` has a common multiple with the length of the alphabet used, this
        cipher is not invertible.
    """

    msg = msg.lower()
    encrypted = ""

    for char in msg:
        try:
            idx = ABC.index(char)
            new_idx = (a*idx + b) % len(ABC)
            encrypted += ABC[new_idx]
        except ValueError:
            encrypted += char

    return encrypted

def multiplicative_inverse(a, mod):
    """Tries to find the multiplicative inverse of `a` modulo mod.
    
    Returns 0 if no inverse exists (i.e. if gcd(a, mod) > 1).
    """

    for inv in range(mod - 1, -1, -1):
        if (inv * a) % mod == 1:
            break

    return inv

def decrypt(a, b, msg):
    """Decrypt a message encrypted with the affine cypher.

    We assume `a` is the multiplicative constant and `b` is additive.
    Raises an error if `a` cannot be inverted.

    y = ax + b \iff y - b = ax \iff inv(a)*(y - b) = x
    """

    msg = msg.lower()
    decrypted = ""

    inv = multiplicative_inverse(a, len(ABC))
    if inv == 0:
        raise ValueError(f"{a} cannot be inverted modulo {len(ABC)}.")

    for char in msg:
        try:
            idx = ABC.index(char)
            new_idx = inv*(idx - b) % len(ABC)
            decrypted += ABC[new_idx]
        except ValueError:
            decrypted += char

    return decrypted


if __name__ == "__main__":

    example = "The quick, brown, fox jumps (!) over the lazy dog."
    a, b = 3, 10

    print(f"Original message:")
    print(f"\t{example}")
    print(f"Encrypt with {a}x + {b}:")

    encrypted = encrypt(a, b, example)
    print(f"\t{encrypted}")

    print(f"The inverse of {a} modulo {len(ABC)} is {multiplicative_inverse(a, len(ABC))}.")
    print("The decryption is:")
    print(f"\t{decrypt(a, b, encrypted)}")

    print("\n" + "#"*40 + "\n")
    
    acc = 0
    for a in range(len(ABC)):
        for b in range(len(ABC)):
            try:
                acc += 1
            except ValueError:
                pass
    print(f"Brute-forcing would take {acc} attempts.")