ABC = "abcdefghijklmnopqrstuvwxyz"

def encrypt(key, msg):
    """Encrypt a message with the given key with the Caesar cipher."""

    msg = msg.lower()
    encrypted = ""
    
    for char in msg:
        try:
            idx = ABC.index(char)
            new_idx = (idx + key) % len(ABC)
            encrypted += ABC[new_idx]
        except ValueError:
            encrypted += char

    return encrypted

def decrypt_dup(key, msg):
    """Decrypt a message that was encrypted with the given key."""

    msg = msg.lower()
    decrypted = ""

    for char in msg:
        try:
            idx = ABC.index(char)
            new_idx = (idx - key) % len(ABC)
            decrypted += ABC[new_idx]
        except ValueError:
            decrypted += char

    return decrypted

def decrypt(key, msg):
    """Decrypt a message that was encrypted with the given key."""

    return encrypt(len(ABC) - key, msg)

def brute_force(msg):
    """Decrypt a message by brute-force."""

    padding = len(str(len(ABC) - 1))

    for key, char in enumerate(ABC):
        decrypted = decrypt(key, msg)
        
        print(f"{str(key).ljust(padding)} - {char} - {decrypted}")


if __name__ == "__main__":

    example = "The quick, brownk, fox jumps (!) over the lazy dog."

    print("Original message:")
    print(f"\t{example}\n")
    
    print("Encryptions:")
    for key in range(len(ABC)):
        print(f"\t{key} - {encrypt(key, example)}")

    print("\n" + "#"*40 + "\n")

    key = 8
    encrypted = encrypt(key, example)
    print(f"With key {key} we got '{encrypted}', now we use brute-force:")
    brute_force(encrypted)