from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Key (16 bytes = 128 bits)
key = b'\x00' * 16

# Initialization Vector (IV)
iv = b'\x01' * 12

# Message
data = b"IntegrityCheck"

# Create AES-GCM object (GMAC uses only authentication)
aesgcm = AESGCM(key)

# Generate authentication tag (without encryption)
# Passing empty plaintext still produces a valid GMAC tag
tag = aesgcm.encrypt(iv, b'', data)[-16:]  # last 16 bytes = tag
print("GMAC Tag:", tag.hex())
