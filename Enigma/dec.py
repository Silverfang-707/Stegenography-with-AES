import random

# Define the Enigma machine'&#x27;s components
ROTOR1_WIRING = {'A': 'E', 'B': 'K', 'C': 'Q', 'D': 'G', 'E': 'N', 'F': 'Y', 'G': 'U', 'H': 'J', 'I': 'P', 'J':
'S', 'K': 'X', 'L': 'R', 'M': 'T', 'N': 'W', 'O': 'V', 'P': 'B', 'Q': 'C', 'R': 'D', 'S': 'F', 'T': 'H', 'U': 'I',
'V': 'L', 'W': 'M', 'X': 'O', 'Y': 'P', 'Z': 'Z'}
ROTOR2_WIRING = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J', 'J':
'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V',
'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'}
ROTOR3_WIRING = {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J':
'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z',
'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'}

def enigma_decrypt(encrypted_message, rotor_settings):
    # Initialize the decrypted message
    decrypted_message = []

    # Iterate through each character in the encrypted message
    for char in encrypted_message:
        # Convert to uppercase (since Enigma only works with uppercase letters)
        char = char.upper()

        # Apply the Rotor 3 substitution in reverse order
        if char in ROTOR3_WIRING:
            char = ROTOR3_WIRING.get(char)

        # Apply the Rotor 2 substitution in reverse order
        if char in ROTOR2_WIRING:
            char = ROTOR2_WIRING.get(char)

        # Apply the Rotor 1 substitution in reverse order
        if char in ROTOR1_WIRING:
            char = ROTOR1_WIRING.get(char)

        # Add the decrypted character to the message
        decrypted_message.append(char)

    return ''.join(decrypted_message)

# Test the Enigma decryption function
encrypted_message = "NTLN"
rotor_settings = {"R1": 5, "R2": 7, "R3": 12}
decrypted_message = enigma_decrypt(encrypted_message, rotor_settings)
print(f"Decrypted message: {decrypted_message}")