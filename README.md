---

# Image Steganography with AES Encryption

This Python script allows users to perform steganography, hiding encrypted messages within images using the Advanced Encryption Standard (AES) algorithm. It provides functionality for both encoding messages into images and decoding messages from encoded images.

## Features

- **Encode Message:** Embeds a message (after AES encryption) into an image using the least significant bit (LSB) technique.
- **Decode Message:** Extracts and decrypts a hidden message from an encoded image.

## Dependencies

- **PIL (Python Imaging Library):** Used for image manipulation.
- **PyCryptodome:** A Python library that provides cryptographic functions. Specifically, it uses `AES` from `Crypto.Cipher` for encryption and decryption.

## How to Use

1. **Clone Repository:** Clone this repository to your local machine.
2. **Install Dependencies:** Install the necessary dependencies by running `pip install -r requirements.txt`.
3. **Run the Script:** Execute `main.py` using Python. Follow the prompts to either encode or decode a message.
    ```bash
    python main.py
    ```
4. **Encryption Key:** Ensure you provide the same encryption key during both encoding and decoding phases to successfully retrieve the original message.

## Usage Examples

- **Encoding a Message:**
    ```python
    Enter if you want to Encrypt(E) or Decrypt(D): E
    Enter the Image Path(with Extension): path/to/image.png
    Enter your Message: Your secret message here
    Enter key: your_secret_key
    ```

- **Decoding a Message:**
    ```python
    Enter if you want to Encrypt(E) or Decrypt(D): D
    Enter the Encoded Image Path(with Extension): path/to/encoded_image.png
    Enter key: your_secret_key
    ```

## Note

- This is just a simple implementation and is not secure for professional purposes

## Author

- [Silverfang](github.com/Silverfang-707)

Feel free to contribute by opening issues or pull requests!

--- 
