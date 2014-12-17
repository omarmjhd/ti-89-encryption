class EncryptionEngine:

    encode_dict = {'a': '=', 'b': '(', 'c': ')', 'd': ',', 'e': '/', 'f': '|', 'g': '7', 'h': '8', 'i': '9', 'j': '*',
                      'k': '<', 'l': '4', 'm': '5', 'n': '6', 'o': '-', 'p': ';', 'q': '1', 'r': '2', 's': '3', 't': 't',
                      'u': '+', 'v': '0', 'w': '.', 'x': 'x', 'y': 'y', 'z': 'z', '.': '>', ',': '[', ' ': ']', '_': '_',
                      '?': '@', '!': '#', '&': '&'}

    decode_dict = {'=': 'a', '(': 'b', ')': 'c', ',': 'd', '/': 'e', '|': 'f', '7': 'g', '8': 'h', '9': 'i', '*': 'j',
                      '<': 'k', '4': 'l', '5': 'm', '6': 'n', '-': 'o', ';': 'p', '1': 'q', '2': 'r', '3': 's', 't': 't',
                      '+': 'u', '0': 'v', '.': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '>': '.', '[': ',', ']': ' ', '_': '_',
                      '@': '?', '#': '!', '&': '&'}

    def __init__(self):

        EncryptionEngine.encode_dict = EncryptionEngine.encode_dict
        EncryptionEngine.decode_dict = EncryptionEngine.decode_dict

    def encode_char(self, char):

        return EncryptionEngine.encode_dict[char]

    def decode_char(self, char):

        return EncryptionEngine.decode_dict[char]

    def encode_string(self, string):

        encoded_string = ''
        string = string.lower()
        string = string.replace('\n', '&')

        for i in range(0, len(string)):

            encoded_string += self.encode_char(string[i])

        return encoded_string

    def decode_string(self, string):

        decoded_string = ''

        for i in range(0, len(string)):

            decoded_string += self.decode_char(string[i])

        decoded_string = decoded_string.replace('&', '\n')

        return decoded_string

    def write_string_to_file(self, string):

        file_title = input("What would you like to call the file?: ") + '.txt'

        file = open(file_title, "w")

        file.write(string)

        file.close()

    def encode_file(self, string):

        file_title = string + ".txt"
        file = open(file_title, 'r')
        text = file.read()
        file.close()

        encoded_string = EncryptionEngine.encode_string(self, text)

        print("Your file has been encoded as follows: " + encoded_string)
        print()

        new_title = string + "_encoded.txt"
        encoded_file = open(new_title, "w")
        encoded_file.write(encoded_string)
        encoded_file.close()

        print("Your encoded file has been saved as: " + new_title)

    def decode_file(self, string):


        file_title = string + ".txt"
        file = open(file_title, 'r')
        text = file.read()
        file.close()

        decoded_string = EncryptionEngine.decode_string(self, text)

        print("Your file has been decoded as follows: " + decoded_string)
        print()

        new_title = string + "_decoded.txt"
        encoded_file = open(new_title, "w")
        encoded_file.write(decoded_string)
        encoded_file.close()

        print("Your decoded file has been saved as: " + new_title)








