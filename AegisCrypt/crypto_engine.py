import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class CryptoEngine:

    @staticmethod
    def derive_key(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000
        )
        return kdf.derive(password.encode())

    @staticmethod
    def encrypt_file(path, password):
        salt = os.urandom(16)
        nonce = os.urandom(12)

        with open(path, "rb") as f:
            data = f.read()

        key = CryptoEngine.derive_key(password, salt)

        aes = AESGCM(key)

        encrypted = aes.encrypt(
            nonce,
            data,
            None
        )

        output = path + ".enc"

        with open(output, "wb") as f:
            f.write(salt + nonce + encrypted)

        return output

    @staticmethod
    def decrypt_file(path, password):

        with open(path, "rb") as f:
            data = f.read()

        salt = data[:16]
        nonce = data[16:28]
        encrypted = data[28:]

        key = CryptoEngine.derive_key(password, salt)

        aes = AESGCM(key)

        decrypted = aes.decrypt(
            nonce,
            encrypted,
            None
        )

        output = path.replace(".enc", "")

        with open(output, "wb") as f:
            f.write(decrypted)

        return output
