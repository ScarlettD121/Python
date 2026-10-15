#Scarlett Dowdle
#October 14, 2026
#DESCRIPTION: print a rectangle with a height based on user input

def main():
    height=int(input("How tall would you like the rectangle? "))
    rectangle_builder(height)


def rectangle_builder(height):
    print("*****") # print top layer of the rectangle
    i = 0
    while i < height:
        print("*   *")
        i+=1
    print("*****") # print bottom layer of the rectangle

main()