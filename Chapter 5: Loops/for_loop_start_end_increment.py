#Scarlett Dowdle
#October 7, 2026
#DESCRIPTION: output numbers incramentally between the numbers and an increment given by the user using for a loop.


start=int(input("Starting point: "))
end=int(input("Ending point: "))
increment=int(input("Increment by: "))

if increment<0:
    range_end = end-1
else:
    range_end = end+1


for i in range(start,range_end,increment): #each number in the range [start, end] incrementing by increment
    print(i, end=' ') #ends each print with a space instead of a line break