from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

key = "SecretKey1234567"
encrypted_flag = "96a0299d6c60cd0f40218b73ab5fc4b710b8951bd0ed8977a1382328454a2ce68106660bb48808c2fa7a141ac863732f66f9032d00cf2c0ecc3a6871683911a6"
encrypted_bytes = unhexlify(encrypted_flag)

# Decrypt first block; block size is 16 according to provided script
first_block = encrypted_bytes[:16]
decrypted_first_block = AES.new(key.encode(), AES.MODE_ECB).decrypt(first_block)

# Compute IV using decrypted first block and known plaintext
known_plaintext = b"Here is the flag for you: "
iv_list = []
for i in range(16):
  iv_list.append(decrypted_first_block[i] ^ known_plaintext[i])
iv = bytes(iv_list)

# Decrypt complete ciphertext
padded_flag = AES.new(key.encode(), AES.MODE_CBC, iv).decrypt(encrypted_bytes)
flag = unpad(padded_flag, 16)

print(flag.decode())
