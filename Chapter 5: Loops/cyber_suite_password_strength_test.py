#Scarlett Dowdle
#October 14, 2026
#DESCRIPTION: Evaluate the strength of a user inputed password and give a score and tips for improvment
import string

string.symbols = '!@#$%^&*()-_=+[]{}|;:\'\\",.<>/?'

def main():
    print("===== PASSWORD STRENGTH CHECKER =====\nThis tool analyzes your password and rates its strength.\n")
    password = input("Enter a password to check: ")
    pass_Analysis(password)


def pass_Analysis(password):
    lowercase = 0
    uppercase = 0
    digits = 0
    symbols = 0
    length = 0

    for character in password:
        if character in string.ascii_lowercase:
            lowercase += 1
        if character in string.ascii_uppercase:
            uppercase += 1
        if character in string.digits:
            digits += 1
        if character in string.symbols:
            symbols += 1
        length += 1
    print("\n===== PASSWORD ANALYSIS =====")
    print(f"Length: {length} characters")
    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)
    print("Digits:", digits)
    print("Special characters:", symbols)
    pass_Scoring(lowercase,uppercase,digits,symbols,length)



def pass_Scoring(lower,upper,digits,symbols,length):
    print()
    score = 0
    character_types = 0

    #Length Factor:
    if length >= 12:
        score += 25
    elif length in range(8,12): #length is 8 to 11 characters long
        score += 15
    elif length in range(6,8): #length is 6 to 7 characters long
        score += 10

    #Character Variety:
    if upper >= 1: #Contains at least one uppercase letter
        score += 15
        character_types += 1
    if lower >= 1: #Contains at least one lowercase letter
        score += 15
        character_types += 1
    if digits >= 1: #Contains at least one digit
        score += 15
        character_types += 1
    if symbols >= 1: #Contains at least one special character
        score += 15
        character_types += 1

    #Character Type Diversity:
    if character_types >= 3: #Uses 3 or more different character types
        score += 15
    
    print(f"Security Score: {score}/100")
    if score in range(80,101):
        print("Strength Assessment: STRONG")
    elif score in range(60,80):
        print("Strength Assessment: MODERATE")
    elif score in range(40,60):
        print("Strength Assessment: WEAK")
    elif score < 40:
        print("Strength Assessment: VERY WEAK")
    
    tips(lower,upper,digits,symbols,length)
    

def tips(lower,upper,digits,symbols,length):
    print("\n ===== IMPROVEMENT SUGGESTIONS =====")

    tips_given = False

    if length < 12:
        print("- Use at least 12 characters for better security")
        tips_given = True
    if upper == 0:
        print("- Add uppercase letters (A-Z)")
        tips_given = True
    if lower == 0:
        print("- Add lowercase letters (a-z)")
        tips_given = True
    if digits == 0:
        print("- Add numbers (0-9)")
        tips_given = True
    if symbols == 0:
        print("- Add special characters (!@#$%^&*)")
        tips_given = True

    if tips_given == False:
        print("- Excellent password! Remember to use different passwords for different accounts.")


main()