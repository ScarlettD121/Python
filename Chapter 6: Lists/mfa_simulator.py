#Scarlett Dowdle
#October 25, 2026
#DESCRIPTION: simulate MFA backup code generation and request a valid code
import random

codes = []

def main():
    seed = int(input("ENTER SEED FOR SIMULATION: "))
    print()
    print("===============================\n  SIMULATING CODE GENERATION   \n===============================")
    print()
    gen_codes(seed)
    print()
    print("===============================\n     SIMULATING CODE USE       \n===============================")
    request_code()
    

def gen_codes(seed):
    random.seed(seed)
    for i in range(10):
        num = random.randint(100000,1000000)
        codes.append(num)
    for code in codes:
        print("Backup code:",code)



def request_code():
    print()
    print(f"You have {len(codes)} codes remaining.")
    code = int(input("Enter a valid code: "))
    print()
    if code in codes:
        print("Access Granted")
        print()
        codes.remove(code)
        print(f"You have {len(codes)} codes remaining.")
        print()
        for i in codes:
            print("Backup code:",i)
    elif code not in codes:
        print("Access Denied")


main()