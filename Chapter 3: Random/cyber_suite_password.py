#Scarlett Dowdle
#September 23, 2026
#DESCRIPTION: generate a random password example "!eWtI21@" based on a seed given by user input and output it to the console
import random
import string


def main():
    seed = int(input("Enter a seed for the random number generation: ")) #gets the random seed as an integer from the user
    generate_password(seed)

def generate_password(seed):
    random.seed(seed)
    password = random.choice("!@#$&(),-_") + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.digits) + random.choice("!@#$&(),-_")
    # "!@#$&(),-_" + "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "0123456789" + "!@#$&(),-_"
    print("Your random password is:")
    print(password)

main()