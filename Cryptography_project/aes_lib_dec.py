from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def key_convert(key):
    # conditions to make the key size 32 chars long
    len_padding = 32-len(key)
    if len(key) < 32:
        while len_padding!=0:
            key += "0"
            len_padding-=1

    elif len(asc)==32:
        key = key

    else:
        key = key[:32]

    return key

def decrypt_text(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode().strip()

# User input
cipher_text = input("Enter the cipher text: ")

# User input key
key = input("Enter key:")

# converting the key to 32 chars
key = key_convert(key).encode()
print(key)
# Decrypt the text
decrypted_text = decrypt_text(cipher_text, key)
# print("Decrypted Text:", decrypted_text)