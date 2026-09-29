#Scarlett Dowdle
#September 28, 2026
#DESCRIPTION: print a compliment if the user inputs "yes" and print "No compliment for you!" if the input is not "yes"


user_input = input("Would you like a compliment? ") #ask the user if they would like a compliment and store answer in user_input

if user_input == "yes": #check if the input is exactly "yes"
    print("You have wonderful eyes.") #if input is "yes" print compliment
else:
    print("No compliment for you!") #if input is not exactly "yes" print "No compliment for you!"

print("Thank you for playing.") #always print Thank you for playing as last output.