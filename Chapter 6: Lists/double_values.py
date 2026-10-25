#Scarlett Dowdle
#October 20, 2026
#DESCRIPTION: Sort, double and output the values in a list of numbers given by the user

nums = int(input("How many numbers will you be entering? "))
number_list = []
number_list_doubled = []

for i in range(nums):
    number = (int(input("What is number? ")))
    number_list.append(number)
    number_list_doubled.append(number*2)

print()
print("ORIGINAL -         ", number_list)
number_list.sort()
print("ORIGINAL (sorted) -", number_list)
number_list_doubled.sort()
print("DOUBLED -          ", number_list_doubled)