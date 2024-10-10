def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def pad_message(message):
    # Step 1: Convert the message to bytes
    message_bytes = message.encode('utf-8')

    # Step 2: Append padding bits
    original_length = len(message_bytes) * 8
    padding_length = (448 - (original_length + 64) % 512) % 512
    padded_message = message_bytes + b'\x80' + b'\x00' * (padding_length // 8)

    # Step 3: Append length bits
    padded_message += original_length.to_bytes(8, 'big')
    return padded_messagep

def md5(message):
    # Initialize buffers
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Pad the message
    padded_message = pad_message(message)

    # Process 512-bit blocks (similar to previous example)

    # Final hash value
    hash_value = (A, B, C, D)
    return b''.join(x.to_bytes(4, 'little') for x in hash_value)

# Example usage
message_text = "Hello, this is my 1000-bit message!"
hashed_result = md5(message_text)
print("MD5 Hash:", hashed_result.hex())
