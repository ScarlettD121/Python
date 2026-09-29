#Scarlett Dowdle
#September 28, 2026
#DESCRIPTION: simulate a coin toss using random number 1-100
import random

result_num = random.randint(1,100) #generates a random number between 1 and 100 (inclusive) stores as result_num

print("===== Coin Flipper =====")

if result_num>=51:
    print("Tails")
else:
    print("Heads")