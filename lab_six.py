# Lab 6 - GitHub lab
# Janelle C
def encode(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        encoded += str(digit)
    return encoded

def decode(password):
    pass

def main():

    encoded = None

    while True:
        print("Menu")
        print("_____________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu selection = int(input("Please enter an option: "))
            if menu_selection == 1:
                password = input("Please enter your password to encode: ")
                encoded = encode(password)
            elif menu_selection == 2:
                pass
            elif menu_selection == 3:
                break

if __name__ == "__main__":
    main()
