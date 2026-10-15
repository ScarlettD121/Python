#Scarlett Dowdle
#October 15, 2026
#DESCRIPTION: simulate port knocking granting access after a specific sequence of connection attempts on various ports

correct_ports = [2222,3333,4444,5555]


def main():
    print("===== PORT KNOCKING FIREWALL SIMULATOR =====\nThis firewall requires a specific sequence of port connections.\nYou have 3 attempts to find the correct sequence.\n(Hint: Enter ports as integers, one at a time)\n")
    port_knocks()

def port_knocks():
    i=0
    ports=[""]
    while i < 3:
        print(f"Attempt {i+1} of 3:")
        print("Enter your port knock sequence. Enter 0 when finished.")
        while ports[-1] != 0:
            ports.append(int(input("Enter port number: ")))
        i = port_check(ports, i)
        ports=[""]




def port_check(ports, i):
    ports.remove("")
    length = ports.index(0)
    ports.pop(-1)
    if ports == correct_ports:
        print("\nFIREWALL RESPONSE: Connection accepted!")
        print("Correct port knocking sequence detected.")
        print("Firewall has opened port 22 for your connection.")
        return 3
    elif ports != correct_ports:
        print("\nFIREWALL RESPONSE: Connection rejected!")
        if length != 4:
            print(f"Your sequence had {length} knocks, but the firewall expects 4.\n")
        else:
            print("Incorrect port knocking sequence.\n")
        i += 1
        if i == 3:
            print("MAXIMUM ATTEMPTS REACHED\nFirewall has blocked your IP address for 30 minutes.\nThe correct sequence was: [2222, 3333, 4444, 5555]")
        return i

main()