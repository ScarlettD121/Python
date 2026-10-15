#Scarlett Dowdle
#October 8, 2026
#DESCRIPTION: user inputs a guess for a secret number untiil they guess correctly giving if the guess is higher or lower than the secret number

SECRET_NUM = 33
guess = 0
i = 0

while guess != SECRET_NUM:
    guess = int(input("Guess a number: "))
    if guess < SECRET_NUM:
        print("Your guess is too low.")
    elif guess > SECRET_NUM:
        print("Your guess is too high.")
    i+=1
    print()
if guess == SECRET_NUM:
    print(f"You guessed in {i} tries.")