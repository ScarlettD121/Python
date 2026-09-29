#Scarlett Dowdle
#September 29, 2026
#DESCRIPTION: Checks user provided port number and data transfer speed for its risk


def main():
    print("=== Network Traffic Security Analyzer ===\n")
    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    data_size = int(input("Enter the data transfer size in megabytes (MB): "))
    print("\nFIREWALL LOG:")
    print(f"Port: {port}, Transfer Size: {data_size} MB")
    risk = risk_assessment(port,data_size)
    print("Risk Assessment:",risk)

def risk_assessment(port,size):
    risk_level_3 = "HIGH RISK: Potential unauthorized remote access detected!"
    risk_level_2 = "MEDIUM RISK: Large unencrypted data transfer detected."
    risk_level_1 = "LOW RISK: Secure encrypted transfer detected."
    risk_level_0 = "UNKNOWN: Unrecognized traffic pattern."
    
    if (port == 22 or port == 3389) and (size >= 100):
        return risk_level_3
    #checks if port is 22 or 3389 and size is also 100MB or more, and returns "HIGH RISK: Potential unauthorized remote access detected!"

    elif port == 80 and size > 100:
        return risk_level_2
    #checks if port is 80 and size is also more than 100MB, and returns "MEDIUM RISK: Large unencrypted data transfer detected."

    elif port == 443:
        return risk_level_1
    #checks if port is 443, and returns "LOW RISK: Secure encrypted transfer detected."

    else:
        return risk_level_0
    #if conditions are not met return "UNKNOWN: Unrecognized traffic pattern."

main()