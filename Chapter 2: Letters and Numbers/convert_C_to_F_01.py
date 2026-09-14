#Scarlett Dowdle
#September 14, 2026
#DESCRIPTION: Output degrees Fahrenheit based on user input of degrees Celsius

deg_celsius = float(input("Enter a temperature in Celsius: "))#get temperature in degrees Celsius form user

deg_fahrenheit = deg_celsius*9/5+32 #converts celsius to fahrenheit

print(f"{deg_celsius} degrees Celsius is {deg_fahrenheit} degrees Fahrenheit.") #expected output "[°C] degrees Celsius is [°C in °F] degrees Fahrenheit."