while True:
    string = input("Please type in a word to check if it is a palindrome:")
    if string == "q":
        # exit_condition = False
        print("Exiting...")
        break

    if string == string[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")