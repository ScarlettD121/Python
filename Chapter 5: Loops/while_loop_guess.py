#Scarlett Dowdle
#October 8, 2026
#DESCRIPTION: user inputs a guess for a secret number untiil they guess correctly.

secret_num = 33
guess = 0
i = 0

while guess != secret_num:
    guess = int(input("Guess a number: "))
    i+=1
if guess == secret_num:
    print(f"You guessed in {i} tries.")