encode_dict = {'a': '=', 'b': '(', 'c': ')', 'd': ',', 'e': '/', 'f': '|', 'g': '7', 'h': '8', 'i': '9', 'j': '*',
                  'k': '<', 'l': '4', 'm': '5', 'n': '6', 'o': '-', 'p': ';', 'q': '1', 'r': '2', 's': '3', 't': 't',
                  'u': '+', 'v': '0', 'w': '.', 'x': 'x', 'y': 'y', 'z': 'z', '.': '>', ',': '[', ' ': ']'}

decode_dict = {'=': 'a', '(': 'b', ')': 'c', ',': 'd', '/': 'e', '|': 'f', '7': 'g', '8': 'h', '9': 'i', '*': 'j',
                  '<': 'k', '4': 'l', '5': 'm', '6': 'n', '-': 'o', ';': 'p', '1': 'q', '2': 'r', '3': 's', 't': 't',
                  '+': 'u', '0': 'v', '.': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '>': '.', '[': ',', ']': ' '}


def encode_char(char):

    return encode_dict[char]


def decode_char(char):

    return decode_dict[char]


def encode_string(string):

    encoded_string = ''

    for i in range(0, len(string)):

        encoded_string += encode_char(string[i])

    return encoded_string


def decode_string(string):

    decoded_string = ''

    for i in range(0, len(string)):

        decoded_string += decode_char(string[i])

    return decoded_string



def run():

    user_input = input("Welcome to the TI-89 Encoder and Decoder! "
                       "Would you like to encode(1) or decode(2) or quit(q)?: ")

    if user_input == "1":

        string_to_encode = input("What string would you like to encode? (lowercase, comma, and period only): ")

        encoded_string = encode_string(string_to_encode)

        print("Here is your encoded string: " + encoded_string)

    elif user_input == "2":

        string_to_decode = input("What string would you like to decode? (lowercase, comma, and period only): ")

        decoded_string = decode_string(string_to_decode)

        print("Here is your decoded string: " + decoded_string)

    if user_input == "q":

        return

    run()


run()
"""
string_to_encode = 'hello'

print(string_to_encode)

ec_string = encode_string(string_to_encode)

print(ec_string)

string_to_decode = ec_string
dc_string = decode_string(string_to_decode)

print(dc_string)"""