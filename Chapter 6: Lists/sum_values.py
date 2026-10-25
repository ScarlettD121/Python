#Scarlett Dowdle
#October 23, 2026
#DESCRIPTION: get failed login attempts from the user for each day and provide the total failed attempts for the week and see if over threshold

print("Please enter failed login attempts\n==================================\n")

failed_attempt_numbers = []

failed_attempt_numbers.append(int(input("  Monday:    ")))
failed_attempt_numbers.append(int(input("  Tuesday:   ")))
failed_attempt_numbers.append(int(input("  Wednesday: ")))
failed_attempt_numbers.append(int(input("  Thursday:  ")))
failed_attempt_numbers.append(int(input("  Friday:    ")))

total_failed_attempts = sum(failed_attempt_numbers)
print()
print()
print("===== FAILED LOGIN ATTEMPTS ANALYZER =====\n")
print("Total failed login attempts for the week:", total_failed_attempts)
print()

if total_failed_attempts > 100:
    print("SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!\nRecommendation: Investigate for potential brute force attacks.")
else:
    print("Everything seems normal. It's quiet. Too quiet.\nRecommendation: Continue routine monitoring.")