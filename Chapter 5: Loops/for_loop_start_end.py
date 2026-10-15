#Scarlett Dowdle
#October 7, 2026
#DESCRIPTION: output numbers between the numbers given by the user using for a loop.


start=int(input("Starting point: "))
end=int(input("Ending point: "))

for i in range(start,end+1): #each number in the range [start, end]
    print(i, end=' ') #ends each print with a space instead of a line break