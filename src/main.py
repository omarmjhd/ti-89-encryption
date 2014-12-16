from src import encryption_engine

encryptor = encryption_engine.encryption_engine()

def main():

    user_input = input("Welcome to the TI-89 Encryptor! "
                       "Would you like to encode a string(1), decode a string(2), encode a .txt file(3), decode a .txt file(4) or quit(q)?: ")

    if user_input == "1":

        string_to_encode = input("What string would you like to encode? (lowercase, comma, and period only): ")

        encoded_string = encryptor.encode_string(string_to_encode)

        print("Here is your encoded string: " + encoded_string)

    elif user_input == "2":

        string_to_decode = input("What string would you like to decode? (lowercase, comma, and period only): ")

        decoded_string = encryptor.decode_string(string_to_decode)

        print("Here is your decoded string: " + decoded_string)

    elif user_input == "3":

        file_to_encode = input("What file would you like to encode?: ")

        encoded_file = encryptor.encode_file(file_to_encode)

        print("Your file has been encoded!")

    elif user_input == "q":

        print("We hope you enjoyed using the Encryptor!")
        return

    main()


main()