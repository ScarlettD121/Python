#Scarlett Dowdle
#September 14, 2026
#DESCRIPTION: Simulated login page that gets username user id and password from user input. outputs a welcome message and their password as a series of 'X'



user_name = input("Please enter your name: ") #get user's name as a sting
user_id = int(input("Please enter your user id: ")) #get user's ID as an integer
passwd = input("Please enter your password: ")#get user's password as a string

passwd_length = len(passwd) #gives length of the user's password as an integer


print(f"Welcome, {user_name}. Your ID is {user_id}.")
print()
print("PASSWORD: \n" + 'X' * passwd_length)
#expected output:
#"Welcome [user's name]. Your ID is [user's ID]"
#
#"PASSWORD: "
#['X' equal to the length of the user's password]