import re 

def isNetmaskValid(subnet):
    results = re.findall(r"(\d+).(\d+).(\d+).(\d+)", netmask)
    print (str(results) + " length: " + str(len(results[0])))
    if len(results[0]) != 4:
        return False
    current_number = results[0][0]
    for number in results[0]:
        if number > current_number:
            return False
        current_number = number
    return True
    

def get_CIDR_by_netmask(subnet):
    # if not isSubnetValid(subnet):
    #     return False
    bin_mask = ""
    numbers = subnet.split(".")
    for number in numbers:
        bin_mask += bin(int(number))[2:].zfill(8)
    print(bin_mask)
    count_one = bin_mask.count("1")
    return count_one

netmask = input("input netmask: ")

if isNetmaskValid(netmask):
    print ("valid netmask format")
    CIDR = get_CIDR_by_netmask(netmask)
    print ("/{}".format(CIDR))
else:
    print("not a valid netmask format")



