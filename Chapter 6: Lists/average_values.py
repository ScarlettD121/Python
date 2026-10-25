#Scarlett Dowdle
#October 23, 2026
#DESCRIPTION: get integers form the user and provide the sum and average

nums = []

number_input = input('Enter a number ("DONE" to finish): ')
if number_input == "DONE":
    print("ERROR")
    quit()
else:
    number = int(number_input)
    nums.append(number)
while number_input != "DONE":
    number_input = input('Enter a number ("DONE" to finish): ')
    if number_input != "DONE":
        number = int(number_input)
        nums.append(number)

print()
print("---END OF INPUT---")
print()

print ("NUMBERS = ", nums)
num_sum = sum(nums)
print("SUM =", num_sum)
average = num_sum/len(nums)
print("AVERAGE = ", average)