#Scarlett Dowdle
#October 25, 2026
#DESCRIPTION: give a report and score of the users password
import string


def main():
    password = input("Enter your password: ")
    pass_analysis(password)

def pass_analysis(passwd):
    points = [] # points for each type of character. [length,upper,lower,num,special]
    character_ammount = [] # ammount of each type of character. [total,upper,lower,num,special]
    upper = 0
    lower = 0
    digits = 0
    symbols = 0

    character_ammount.insert(0,len(passwd))
    if len(passwd) < 8:
        points.insert(0,0)
    elif len(passwd) in range(8,16):
        points.insert(0,5)
    elif len(passwd) > 15:
        points.insert(0,8)

    for char in passwd:
        if char in string.ascii_uppercase:
            upper += 1
        if char in string.ascii_lowercase:
            lower += 1
        if char in string.digits:
            digits += 1
        if char not in string.ascii_letters and char not in string.digits:
            symbols += 1
        
    character_ammount.insert(1,upper)
    character_ammount.insert(2,lower)
    character_ammount.insert(3,digits)
    character_ammount.insert(4,symbols)

    #upper
    points.insert(1,calc_points(upper))

    #lower
    points.insert(2,calc_points(lower))

    #number
    points.insert(3,calc_points(digits))
    
    #special
    points.insert(4,calc_points(symbols))

    pass_report(points,character_ammount)



def calc_points(char_num):
    if char_num < 1:
        return 0
    elif char_num == 1:
        return 2
    elif char_num == 2:
        return 4
    elif char_num > 2:
        return 8

def pass_report(points, char_ammount):
    print()
    print("Password Analysis Report\n-------------------------")
    print(f"LENGTH: {points[0]} points ({char_ammount[0]} characters)")
    print(f"UPPERCASE: {points[1]} points ({char_ammount[1]} uppercase letter(s))")
    print(f"LOWERCASE: {points[2]} points ({char_ammount[2]} lowercase letter(s))")
    print(f"NUMBERS: {points[3]} points ({char_ammount[3]} number(s))")
    print(f"SPECIAL CHARACTERS: {points[4]} points ({char_ammount[4]} special character(s))")
    print()

    total_score = sum(points)/40
    percentage = total_score * 100
    print("Total Score:",total_score)
    print(f"Strength Percentage: {percentage}%")

main()