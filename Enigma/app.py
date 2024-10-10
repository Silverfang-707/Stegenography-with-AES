class EnigmaMachine:
    def __init__(self, rotor_wirings, reflector_wiring, ring_settings, plugboard_settings):
        self.rotor_wirings = rotor_wirings
        self.reflector = reflector_wiring
        self.ring_settings = ring_settings
        self.plugboard = self.create_plugboard(plugboard_settings)
        self.rotor_positions = [0] * len(self.rotor_wirings)
        self.rotor_notches = ['Q', 'E', 'V', 'J']  # Example notches for each rotor

    def create_plugboard(self, settings):
        plugboard = {chr(i + ord('A')): chr(i + ord('A')) for i in range(26)}
        for pair in settings:
            plugboard[pair[0]] = pair[1]
            plugboard[pair[1]] = pair[0]
        return plugboard

    def rotate_rotors(self):
        # Double-stepping mechanism
        for i in range(len(self.rotor_positions) - 1):
            if chr((self.rotor_positions[i] + ord('A')) % 26) == self.rotor_notches[i]:
                self.rotor_positions[i+1] = (self.rotor_positions[i+1] + 1) % 26
                if i > 0:
                    self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26

        # Always rotate the rightmost rotor
        self.rotor_positions[-1] = (self.rotor_positions[-1] + 1) % 26

    def get_rotor_output(self, input_char, rotor_index, encrypt=True):
        offset = (self.ring_settings[rotor_index] + self.rotor_positions[rotor_index]) % 26
        if encrypt:
            input_index = (ord(input_char) - ord('A') + offset) % 26
            output_char = self.rotor_wirings[rotor_index][input_index]
            output_index = (ord(output_char) - ord('A') - offset) % 26
        else:
            input_index = (ord(input_char) - ord('A') + offset) % 26
            output_index = self.rotor_wirings[rotor_index].index(chr(input_index + ord('A')))
            output_char = chr((output_index - offset) % 26 + ord('A'))
        return output_char

    def encrypt_decrypt_char(self, char, encrypt=True):
        # Pass through the plugboard
        char = self.plugboard[char]
        
        # Pass through the rotors
        for i in range(len(self.rotor_wirings)-1, -1, -1):
            char = self.get_rotor_output(char, i, encrypt)

        # Pass through the reflector
        char = self.reflector[ord(char) - ord('A')]

        # Pass back through the rotors in reverse order
        for i in range(len(self.rotor_wirings)):
            char = self.get_rotor_output(char, i, not encrypt)

        # Pass back through the plugboard
        return self.plugboard[char]

    def process_message(self, message, encrypt=True):
        processed_message = ""
        for char in message.upper():
            if char.isalpha():
                self.rotate_rotors()
                processed_message += self.encrypt_decrypt_char(char, encrypt)
            else:
                processed_message += char  # Non-alphabetic characters are not encrypted/decrypted
        return processed_message

    def set_rotor_positions(self, message_key):
        for i in range(len(self.rotor_positions)):
            self.rotor_positions[i] = ord(message_key[i]) - ord('A')

# Example usage with user inputs:
rotor_wirings_input = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I wiring example
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II wiring example
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",  # Rotor III wiring example
    "ESOVPZJAYQUIRHXLNFTGKDCMWB"   # Rotor IV wiring example (for Naval M4 version)
]
reflector_wiring_input = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B example

rotor_wirings_input = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor I wiring example
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor II wiring example
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",  # Rotor III wiring example
    "ESOVPZJAYQUIRHXLNFTGKDCMWB"   # Rotor IV wiring example (for Naval M4 version)
]
reflector_wiring_input = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B example

ring_settings_input = [1, 1, 1, 1]  # Example ring settings for each rotor
plugboard_settings_input = [('A', 'B'), ('C', 'D')]  # Example plugboard settings

# Initialize the Enigma machine with user inputs
enigma_machine = EnigmaMachine(rotor_wirings_input, reflector_wiring_input, ring_settings_input, plugboard_settings_input)

# Set the initial rotor positions using a message key
message_key_input = "ABCD"  # Example message key
enigma_machine.set_rotor_positions(message_key_input)

# Encrypt or decrypt a message
message_to_process = "HELLOWORLD"  # Example message
encrypted_message = enigma_machine.process_message(message_to_process)
print("Encrypted Message:", encrypted_message)

# To decrypt, reset the rotor positions and process the encrypted message
enigma_machine.set_rotor_positions(message_key_input)
decrypted_message = enigma_machine.process_message(encrypted_message, encrypt=False)
print("Decrypted Message:", decrypted_message)
