from PIL import Image

def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

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

if __name__ == "__main__":
    image_path = input("Enter the image file name (with extension): ")
    message = input("Enter the message to be encoded: ")
    
    # Encoding the message
    encode_message(image_path, message)
    print("Message encoded successfully!")
