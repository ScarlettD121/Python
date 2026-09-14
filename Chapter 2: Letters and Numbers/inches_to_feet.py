#Scarlett Dowdle
#September 14, 2026
#DESCRIPTION: Output feet and inches based on inches provided by user input

input_inches = int(input("Enter the number of inches: ")) #get inches from user as a interger

output_feet = input_inches // 12 #gives the number of full feet from the inches provided
output_inches = input_inches % 12 #gives the remaining inches 

print(f"{input_inches} inches is {output_feet} feet, and {output_inches} inches") #expected output "[inches inputed] inches is [full feet] feet, and [remaining inches] inches"