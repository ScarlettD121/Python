#Scarlett Dowdle
#October 14, 2026
#DESCRIPTION: Check if the user inputs the correct password, is so grant access.

PASSWD="tooManySecrets"


def main():
    pass_attempt = input("Enter password: ")
    authenticate(pass_attempt)


def authenticate(pass_attempt):
    while pass_attempt != PASSWD:
        print()
        print("Password does not match.")
        pass_attempt = input("Enter password: ")
    if pass_attempt == PASSWD:
        print()
        print("Access granted.")

main()

