import random

sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

invsbox = [0 for i in range(256)]
for i in range(256):
    invsbox[sbox[i]] = i

def binary(n):
    A = []
    a = n
    for i in range(8):
        x = a % 2
        A.append(x)
        a = int((a - x) / 2)
    B = [A[7 - i] for i in range(8)]
    return B

def integer(l):
    a = 0
    for i in range(len(l)):
        a += l[i] * (2 ** (len(l) - i - 1))
    return a

def printf(Matrix):
    text_output = ""
    for i in range(4):
        for j in range(4):
            text_output += chr(integer(Matrix[i][j]))
            text_output += " "
        if i != 3:
            text_output += "\n"
    text_output += "\n-----------------\n"
    return text_output

def xor(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        if (arr1[i] == 0 and arr2[i] == 0) or (arr1[i] == 1 and arr2[i] == 1):
            temp.append(0)
        else:
            temp.append(1)
    return temp

def matrixsplitter(C):
    tempMatrix = []
    for i in range(16):
        temp = []
        for j in range(8):
            temp.append(C[i * 8 + j])
        tempMatrix.append(temp)
    Matrix = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(tempMatrix[i * 4 + j])
        Matrix.append(temp)
    return Matrix

def matrixcombiner(Matrix):
    temp = []
    for i in range(4):
        for j in range(4):
            for k in range(8):
                temp.append(Matrix[i][j][k])
    return temp

def subbytes(S):
    T = [0 for i in range(128)]
    for i in range(16):
        a = 0
        for j in range(8):
            a += S[8 * i + j] * (2 ** (7 - j))  # converting the binary 8 bit to integer
        A = binary(sbox[a])
        for j in range(8):
            T[8 * i + j] = A[j]
    return T

def invsubbytes(S):
    T = [0 for i in range(128)]
    for i in range(16):
        a = 0
        for j in range(8):
            a += S[8 * i + j] * (2 ** (7 - j))
        A = binary(invsbox[a])
        for j in range(8):
            T[8 * i + j] = A[j]
    return T

def Encrypt(P, Key):
    C = subbytes(P)
    C1 = Shiftrows(matrixsplitter(C))
    C2 = Shiftcolumns(C1)
    return matrixcombiner(C2)

def Decrypt(C, Key):
    C1 = InverseShiftcolumns(matrixsplitter(C))
    C2 = InverseShiftrows(C1)
    C3 = invsubbytes(matrixcombiner(C2))
    return C3

def rotate(row, places, direction):
    n = len(row)
    if direction == 1:  # Rotate left
        return row[places % n:] + row[:places % n]
    elif direction == -1:  # Rotate right
        return row[-places % n:] + row[:-places % n]

def Shiftrows(Matrix):
    for i in range(4):
        Matrix[i] = rotate(Matrix[i], i + 1, 1)
    return Matrix

def InverseShiftrows(Matrix):
    for i in range(4):
        Matrix[i] = rotate(Matrix[i], i + 1, -1)
    return Matrix

def Shiftcolumns(Matrix):
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(Matrix[j][i])
        temp = rotate(temp, i + 1, 1)
        for j in range(4):
            Matrix[j][i] = temp[j]
    return Matrix

def InverseShiftcolumns(Matrix):
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(Matrix[j][i])
        temp = rotate(temp, i + 1, -1)
        for j in range(4):
            Matrix[j][i] = temp[j]
    return Matrix

def get_binary_input(text):
    binary_text = []
    for char in text:
        binary_char = binary(ord(char))
        binary_text.extend(binary_char)
    return binary_text

def get_text_output(binary_text):
    text_output = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        byte_string = ''.join(map(str, byte))
        text_output += chr(int(byte_string, 2))
    return text_output

def get_key():
    key_text = input("Enter your key: ")
    key_binary = get_binary_input(key_text)
    # Pad key to 128 bits if shorter
    if len(key_binary) < 128:
        key_binary.extend([0] * (128 - len(key_binary)))
    return key_binary[:128]  # Ensure key length is exactly 128 bits

# Decryption Function
def decrypt_cipher(cipher_text, key):
    cipher_binary = list(map(int, cipher_text.strip()))
    key_binary = key
    original_text_binary = cipher_binary

    # Generate the round keys
    round_keys = []
    for i in range(11):
        round_keys.append(key_binary)
        key_binary = Encrypt(key_binary, key_binary)

    # Decrypt the cipher text
    for i in range(9, -1, -1):
        cipher_binary = xor(cipher_binary, round_keys[i])
        cipher_binary = Decrypt(cipher_binary, round_keys[i])

    decrypted_text_output = get_text_output(cipher_binary)
    return decrypted_text_output

# Main Program
def main():
    # User Input
    cipher_text_input = input("Enter the cipher text: ")

    # Get the key
    key = get_key()

    # Decrypt the cipher text
    decrypted_text = decrypt_cipher(cipher_text_input, key)

    # Output the decrypted text
    print("Decrypted Text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
