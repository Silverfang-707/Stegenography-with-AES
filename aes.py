from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

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
 
def encrypt_text(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + cipher_text).decode()

def decrypt_text(cipher_text, key):
    cipher_text = base64.b64decode(cipher_text.encode())
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode().strip()

def main():
    # User input for key
    key = input("Enter your key (32 characters): ")
    key = key_convert(key).encode()

    # User input for text
    plain_text = input("Enter your text: ")

    # Encrypt the text
    cipher_text = encrypt_text(plain_text, key)
    print("Cipher Text:", cipher_text)

    # Decrypt the text
    decrypted_text = decrypt_text(cipher_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
