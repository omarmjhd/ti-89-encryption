from src import EncryptionEngine

encryptor = EncryptionEngine.EncryptionEngine()


def main():

    user_input = input("Welcome to the TI-89 Encryptor! "
                       "Would you like to encode a string(1), decode a string(2),"
                       " encode a .txt file(3), decode a .txt file(4) or quit(q)?: ")

    if user_input == "1":

        print()
        string_to_encode = input("What string would you like to encode? (Upper or"
                                 "lowercase and comma, or period only): ")

        encoded_string = encryptor.encode_string(string_to_encode)

        print()
        print("Here is your encoded string: " + encoded_string)

        print()
        string_to_file = input("Would you like to write your encoded string to a file? Yes(1), No(2): ")

        if string_to_file == "1":

            encryptor.write_string_to_file(encoded_string)

            print()
            print("Your encoded string has been saved!")

    elif user_input == "2":

        print()
        string_to_decode = input("What string would you like to decode? (lowercase, comma, and period only): ")

        decoded_string = encryptor.decode_string(string_to_decode)

        print()
        print("Here is your decoded string: " + decoded_string)

        print()
        string_to_file = input("Would you like to write your decoded string to a file? Yes(1), No(2): ")

        if string_to_file == "1":

            encryptor.write_string_to_file(decoded_string)

            print()
            print("Your decoded string has been saved!")

    elif user_input == "3":

        print()
        file = input("What is the title of your file?: ")

        encryptor.encode_file(file)

    elif user_input == "4":

        print()
        file = input("What is the title of your file?: ")

        encryptor.decode_file(file)

    elif user_input == "q":

        print()
        print("We hope you enjoyed using the Encryptor!")
        return

    elif user_input != "q" or user_input != "1" or user_input != "2" or user_input != "3" or user_input != "4":

        print()
        print("Sorry, that is not a valid option!")
        print()
        main()

    print()
    main()


main()