#Scarlett Dowdle
#September 29, 2026
#DESCRIPTION: Covert number grade from user input to a letter grade

print("===== Grade Converter =====")
num_grade = int(input("Enter a numerical grade (1-100): "))

if num_grade < 65: #checks if the inputed grade is below 65
    letter_grade = "F"
elif num_grade in range(65,70): #checks if the inputed grade is 65 or above and is below 70
    letter_grade = "D"
elif num_grade in range(70,80): #checks if the inputed grade is 70 or above and is below 80
    letter_grade = "C"
elif num_grade in range(80,90): #checks if the inputed grade is 80 or above and is below 90
    letter_grade = "B"
elif num_grade in range(90,101): #checks if the inputed grade is 90 or above and is below 101
    letter_grade = "A"
elif num_grade > 100: #checks if the inputed grade is above 100
    letter_grade = "A+"
else: #if grade does not fit in any conditions provide response that input is invalid
    letter_grade = "INVALID GRADE"

print(letter_grade)