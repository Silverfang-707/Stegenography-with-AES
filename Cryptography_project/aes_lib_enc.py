from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

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
    return cipher.iv + cipher_text

# User input
plain_text = input("Enter your text: ")

# User input key
key = input("Enter key:")
   
# converting the key to 32 chars
key = key_convert(key).encode()
print(key)
# Encrypt the text
cipher_text = encrypt_text(plain_text, key)
print("Cipher Text:", cipher_text)