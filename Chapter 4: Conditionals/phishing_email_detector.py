#Scarlett Dowdle
#September 29, 2026
#DESCRIPTION: Checks user provide subject line for suspicious words and output risk level


def main():
    subject=input("Enter the email subject line: ")
    phishing_check(subject)

def phishing_check(subject):
    if "urgent" in subject.lower():
        risk_level=3
    elif "immediate action required" in subject.lower():
        risk_level=3
    #checks if the subject inputed contains "urgent" or "immediate action required" regardless of capitalization and assigns a risk level of 3

    elif "win" in subject.lower():
        risk_level=2
    elif "free" in subject.lower():
        risk_level=2
    #checks if the subject inputed contains "win" or "free" regardless of capitalization and assigns a risk level of 2

    elif "password reset" in subject.lower():
        risk_level=1
    #checks if the subject inputed contains "password reset" regardless of capitalization and assigns a risk level of 1

    else:
        risk_level=0
    #if none of the suspicious is in the subject assign a risk level of 0

    phishing_output(subject,risk_level)
    
def phishing_output(subject,risk):
    print()
    print("SECURITY ASSESSMENT:")
    if risk==0:
        print("No phishing indicators detected.")
    elif risk==3:
        print("HIGH RISK: Possible phishing attempt.")
    elif risk==2:
        print("MEDIUM RISK: Suspicious offer detected.")
    elif risk==1:
        print("LOW RISK: Verify legitimacy with sender.")
    print("------------------------")
    print(f"Analyzed subject: \"{subject}\"")


main()