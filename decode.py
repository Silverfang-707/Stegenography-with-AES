from PIL import Image

def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

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

if __name__ == "__main__":
    image_path = input("Enter the encoded image file name (with extension): ")
    
    # Decoding the message
    decoded_message = decode_message(image_path)
    if decoded_message:
        print("Decoded message:", decoded_message.rstrip('!'))  # Remove trailing exclamation mark
    else:
        print("No message found in the encoded image.")
