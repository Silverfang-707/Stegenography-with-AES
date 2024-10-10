from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# text to binary
def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

# binary to text
def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

#converting the key to 32 characters
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

# Encoding Into Image
def encode_message(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    # Add an exclamation mark to the message
    message += "!"

    binary_message = text_to_binary(message)
    binary_message += '1111111111111110'  # Adding a sentinel value to mark end of message

    if len(binary_message) > width * height * 3:
        raise ValueError("Message too long to encode in the given image.")

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            img.putpixel((x, y), tuple(pixel))

            if data_index >= len(binary_message):
                img.save("encoded_image.png")
                return

# Decoding the message
def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ""
    sentinel = '1111111111111110'  # Sentinel value to mark end of message
    sentinel_length = len(sentinel)
    sentinel_index = 0  # Tracks the index within the sentinel value

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for value in pixel:
                binary_message += str(value & 1)
                
                # Check for sentinel value to mark end of message
                if binary_message.endswith(sentinel):
                    # Remove the sentinel value before decoding
                    message = binary_to_text(binary_message[:-sentinel_length])
                    return message

    # If the loop completes without finding the sentinel value, return None
    return None

# AES Encryption
def encrypt_text(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + cipher_text).decode()

# AES Decryption
def decrypt_text(cipher_text, key):
    cipher_text = base64.b64decode(cipher_text.encode())
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode().strip()

def main():
    # Ask user if they want to encode or decode
    decision = input("Enter if you want to Encrypt(E) or Decrypt(D): ")
    if(decision.capitalize() == 'E'):
        # Get user Inputs
        image_path = input("Enter the Image Path(with Extenstion): ")
        plain_text = input("Enter your Message: ")
        key = input("Enter key: ")
        key = key_convert(key).encode()
        # Encrypt the message using aes
        cipher_text = encrypt_text(plain_text, key)
        # Embed the cipher into the image
        encode_message(image_path, cipher_text)
    
    elif(decision.capitalize() == 'D'):
        image_path = input("Enter the Encoded Image Path (with Extension): ")
        key = input("Enter key: ")
        key = key_convert(key).encode()

        # Decode the cipher from the image
        decoded_message = decode_message(image_path).rstrip('!')

        # Decrypt the decoded cipher text
        decrypted_text = decrypt_text(decoded_message, key)
        print("Decrypted Text:", decrypted_text)
    
    else:
        print("please provide a valid input")

if __name__ =="__main__":
    main()