#Scarlett Dowdle
#October 25, 2026
#DESCRIPTION: get a list of fortunes from the user and give them randomly
import random



def main():
    print("=======================================")
    print("Welcome to the Fortune Telling Machine!")
    print("=======================================")
    print()
    get_fortunes()


def get_fortunes():
    fortunes = []
    fortune = ""

    print('Enter some fortunes. Type "DONE" when you are through.')
    while fortune != "DONE":
        fortune = input("Enter a fortune: ")
        fortunes.append(fortune)
    fortunes.remove("DONE")
    give_fortunes(fortunes)




def give_fortunes(fortunes):
    print(random.choice(fortunes))
    print()
    give_another_fortune = input("Another fortune (y/n)? ")
    while give_another_fortune == "y":
        print(random.choice(fortunes))
        print()
        give_another_fortune = input("Another fortune (y/n)? ")
    if give_another_fortune == "n":
        print()
        print()
        print("Thank you for using the Fortune Telling Machine!\nSmash that LIKE and Subscribe button and tell your friends!")

main()