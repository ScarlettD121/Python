#Scarlett Dowdle
#October 23, 2026
#DESCRIPTION: Take user inputed customer names and move the first one to the end of the list

customers = []
name = ""

while name != "EOF":
    name = input("Enter the name of the customer: ")
    customers.append(name)
customers.remove("EOF")

print()
print(customers)

name_to_move = customers[0]
customers.pop(0)
customers.append(name_to_move)
print(customers)
