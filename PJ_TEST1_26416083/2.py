slash = input("input netmask format CIDR slash? ")

valid_input = True
try:
    int(slash)
    if int(slash) > 32 or int(slash) < 0:
        print("invalid input")
        valid_input = False
except Exception as e:
    print("invalid input")
    valid_input = False

if valid_input:
    slash_number = int(slash)

    slash_bin = ""

    for i in range (32):
        if i < slash_number:
            slash_bin += "1"
        else:
            slash_bin += "0"

    print("binary: " + slash_bin)

    desimal_netmask = ""
    desimal_netmask += str(int(slash_bin[:8], 2)) + "."
    desimal_netmask += str(int(slash_bin[8:16], 2)) + "."
    desimal_netmask += str(int(slash_bin[16:24], 2)) + "."
    desimal_netmask += str(int(slash_bin[24:32], 2))

    print("decimal: " + desimal_netmask)
