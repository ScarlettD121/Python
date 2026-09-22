#Scarlett Dowdle
#September 22, 2026
#DESCRIPTION: Roll a D6 twice - generate a random integer between 1 and 6 (inclusive) twice based on a seed given by user input and output it to the console
import random

def main():
    seed = int(input("Enter a seed for the random number generation: ")) #gets the random seed as an integer from the user
    roll_die(seed)

def roll_die(seed):
    random.seed(seed)
    print("Die roll one is",random.randint(1,6))
    print("Die roll two is",random.randint(1,6))


main()