class encryption_engine():

    encode_dict = {'a': '=', 'b': '(', 'c': ')', 'd': ',', 'e': '/', 'f': '|', 'g': '7', 'h': '8', 'i': '9', 'j': '*',
                      'k': '<', 'l': '4', 'm': '5', 'n': '6', 'o': '-', 'p': ';', 'q': '1', 'r': '2', 's': '3', 't': 't',
                      'u': '+', 'v': '0', 'w': '.', 'x': 'x', 'y': 'y', 'z': 'z', '.': '>', ',': '[', ' ': ']', '_': '_'}

    decode_dict = {'=': 'a', '(': 'b', ')': 'c', ',': 'd', '/': 'e', '|': 'f', '7': 'g', '8': 'h', '9': 'i', '*': 'j',
                      '<': 'k', '4': 'l', '5': 'm', '6': 'n', '-': 'o', ';': 'p', '1': 'q', '2': 'r', '3': 's', 't': 't',
                      '+': 'u', '0': 'v', '.': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '>': '.', '[': ',', ']': ' ', '_': '_'}

    def __init__(self):


        encryption_engine.encode_dict = encryption_engine.encode_dict
        encryption_engine.decode_dict = encryption_engine.decode_dict

    def encode_char(self, char):

        return encryption_engine.encode_dict[char]


    def decode_char(self, char):

        return encryption_engine.decode_dict[char]


    def encode_string(self, string):

        encoded_string = ''

        for i in range(0, len(string)):

            encoded_string += self.encode_char(string[i])

        return encoded_string


    def decode_string(self, string):

        decoded_string = ''

        for i in range(0, len(string)):

            decoded_string += self.decode_char(string[i])

        return decoded_string

    def encode_file(self, file): # This doesnt work

        file = open(file, "w")

        file_string = file.read()

        encoded_file_string = self.encode_string(file_string)

        encoded_formatted = encoded_file_string.replace('_', '\n')

        file.write(encoded_formatted)

        file.close()


