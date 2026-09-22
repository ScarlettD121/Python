#Scarlett Dowdle
#September 22, 2026
#DESCRIPTION: generate a random integer between 1 and 10 (inclusive) based on a seed given by user input and output it to the console
import random


def main():
    seed = int(input("Enter a seed for the random number generation: ")) #gets the random seed as an integer from the user
    bounded_random(seed) #passes the seed to the bounded_random function

def bounded_random(seed):
    random.seed(seed)
    print(random.randint(1,10)) # prints 1,2,3,4,5,6,7,8,9, or 10

main()