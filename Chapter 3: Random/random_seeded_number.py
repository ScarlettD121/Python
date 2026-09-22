#Scarlett Dowdle
#September 22, 2026
#DESCRIPTION: generate a random number based on a seed given by user input and output it to the console
import random


def main():
    seed = int(input("Enter a seed for the random number generation: "))
    generate_seeded_random_number(seed)



def generate_seeded_random_number(seed):
    random.seed(seed)
    print(random.random())


main()