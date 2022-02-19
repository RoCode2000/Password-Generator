import random
import string

def main():
    print("Hello, welcome to Password Generator")
    length = int(input("\nEnter the length of your desired password: "))
    special = input("\nDo you require special characters in your password? (Y/N): ")
    if special == "y" or special == "Y":
        password = with_special(length)
    else:
        password = no_special(length)
    print(password)


# Print password with special character
def with_special(length):
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    temp = random.choices(all, k = length)
    password = "".join(temp)
    return password


# Print password without special character
def no_special(length):
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits
    temp = random.choices(all, k = length)
    password = "".join(temp)
    return password


main()