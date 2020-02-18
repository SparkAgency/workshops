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