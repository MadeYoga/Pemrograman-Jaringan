import re

def dot_valid(dot_count):
    if dot_count > 3 or dot_count < 3:
        return False
    return True

#def isDigit(val):
#    try:
#        int(val)
#        return True
#    except:
#        return False

ip_addr = input ("input ip address: ")

# CHECK JUMLAH .
dot_count = int(len(re.findall("\.", ip_addr)))

valid = False

if dot_valid(dot_count):

    # hapus SPASI
    ip = re.sub(r' ', '', ip_addr)

    # CHECK ANGKA IP
    ip_numbers = ip.split(".")
    ips = []
    for ip_number in ip_numbers:
        if re.search(r'[a-zA-Z]', ip_number):
            print("found Alphabet")
            valid=False
            break
            
        #if not isDigit(ip_number):
        #    valid = False
        #    break
        ip_number = str(int(ip_number))
        if int(ip_number) < 0 or int(ip_number) > 255:
            valid = False
            break
        ips.append(ip_number)
        ips.append(".")
        valid = True
    if valid:    
        ips.pop()
        ip = ""
        for ip_attr in ips:
            ip += ip_attr
    
if valid:
    print("VALID IP ADDRESS: " + ip)
    if ip_numbers[0] == "10":
        print("PRIVATE IP ADDRESS")
    elif ip_numbers[0] == "192" and ip_numbers[1] == "168":
        print("PRIVATE IP ADDRESS")
    elif ip_numbers[0] == "172" or ip_numbers[0] == "168":
        if ( int(ip_numbers[1]) <= 31 and int(ip_numbers[1]) >= 16 ):
            print("PRIVATE IP ADDRESS")
        else:
            print("PUBLIC IP ADDRESS")
    else:
        print("PUBLIC IP ADDRESS")
else:
    print("Invalid IP ADDRESS")


