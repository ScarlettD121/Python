#Scarlett Dowdle
#October 20, 2026
#DESCRIPTION: Output the values in a user inputed integer list

num_list = []
for i in range(5):
    num_list.append(int(input("Enter a number: ")))

num_list.sort()

print()
print(num_list)
print("Your numbers are:", end=" ")
print(*num_list, sep='  ')