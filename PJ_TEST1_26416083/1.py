
def get_usable_ip(mask : int): 
    pangkat = 32 - mask
    usable_address = 2**pangkat
    return usable_address - 2

slash = input("input: ")
if not int(slash) > 32 and not int(slash) < 0:
    print(str(get_usable_ip(int(slash))) + " usable IP Address")
else:
    print("invalid input!")

