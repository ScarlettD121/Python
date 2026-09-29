#Scarlett Dowdle
#September 28, 2026
#DESCRIPTION: print the users input coverted to Celsius or Fahrenheit based on user selection

print("===== Temperature Converter =====\n")
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius\n")

selection = int(input("Please choose from the above menu: "))
input_temp = float(input("Enter a temperature to convert: "))

if selection == 1:
    output_temp = input_temp* 9/5 + 32 #if user select option 1 convert input_temp from Celsius to Fahrenheit
    print(f"{input_temp} degrees Celsius is {output_temp} degrees Fahrenheit.")
elif selection == 2:
    output_temp = (input_temp - 32 ) * 5/9 #if user select option 2 convert input_temp from Fahrenheit to Celsius
    print(f"{input_temp} degrees Fahrenheit is {output_temp} degrees Celsius.")
else:
    print("Invalid Selection")