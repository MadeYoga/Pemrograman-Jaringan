import re

def get_broadcast_address(ip_address, subnet_mask):

    ## CONVERTS SUBNET TO BINARY
    bin_mask = ""
    numbers = subnet_mask.split('.')
    for number in numbers:
        bin_mask += bin(int(number))[2:].zfill(8)
    subnet_zero_count = bin_mask.count('0')

    ## CONVERTS IP ADDRESS TO BINARY
    bin_ip_addr = ""
    numbers = ip_address.split('.')
    for number in numbers:
        bin_ip_addr += bin(int(number))[2:].zfill(8)

    ## REPLACE LAST N(SUBNET ZERO COUNT) DIGIT TO 1
    bin_list = list(bin_ip_addr)
    for i in range (len(bin_ip_addr)):
        if i >= len(bin_ip_addr) - subnet_zero_count:
            bin_list[i] = '1'

    ## PUT ON RESULTS TEMP VAR
    bin_broadcast_address = ""
    for digit in bin_list:
        bin_broadcast_address += digit
    
    ## CONVERTS BROADCAST ADDRESS, BINARY TO INTEGER
    broadcast_address = str(int(bin_broadcast_address[:8], 2)) + '.'
    broadcast_address += str(int(bin_broadcast_address[8:16],2)) + '.'
    broadcast_address += str(int(bin_broadcast_address[16:24], 2)) + '.'
    broadcast_address += str(int(bin_broadcast_address[24:32], 2))
    return broadcast_address 

def get_network_address(ip_address, subnet_mask):
    ## CONVERTS SUBNET VALUE TO BINARY
    bin_mask = ""
    numbers = subnet_mask.split('.')
    for number in numbers:
        bin_mask += bin(int(number))[2:].zfill(8)
    subnet_zero_count = bin_mask.count('0')

    ## CONVERTS IP ADDRESS TO BINARY
    bin_ip_addr = ""
    numbers = ip_address.split('.')
    for number in numbers:
        bin_ip_addr += bin(int(number))[2:].zfill(8)
    
    ## REPLACE LAST N(SUBNET ZERO COUNT) DIGIT TO 1
    bin_list = list(bin_ip_addr)
    for i in range (len(bin_ip_addr)):
        if i >= len(bin_ip_addr) - subnet_zero_count:
            bin_list[i] = '0'

    ## PUT ON RESULT TEMP VAR
    bin_network_address = ""
    for digit in bin_list:
        bin_network_address += digit
    
    ## CONVERTS NETWORK ADDRESS, BINARY TO INTEGER
    network_address = str(int(bin_network_address[:8], 2)) + '.'
    network_address += str(int(bin_network_address[8:16],2)) + '.'
    network_address += str(int(bin_network_address[16:24], 2)) + '.'
    network_address += str(int(bin_network_address[24:32], 2))
    return network_address 

def isIpValid(ip_addr):
    # CHECK JUMLAH .
    dot_count = int(len(re.findall(r"\.", ip_addr)))
    valid = False
    if dot_count > 3 or dot_count < 3:
        return
    else:
        # HAPUS SPASI
        ip = re.sub(r' ', '', ip_addr)

        # CHECK ANGKA IP
        ip_numbers = ip.split(".")
        ips = []
        for ip_number in ip_numbers:
            try:
                int(ip_number)
            except:
                return False
            ## CHECK ALPHABET
            if re.search(r'[a-zA-Z]', ip_number):
                valid=False
                break
                
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
            return True
        
        return False

def isSubnetValid(subnet_mask):
    if re.search(r'[a-zA-Z]', subnet_mask):
        return False
    if subnet_mask.count('.') > 3 or subnet_mask.count('.') < 3:
        return False
    subnet_mask.replace(" ", "")
    numbers = subnet_mask.split('.')
    binary = ""
    for number in numbers:
        try:
            int(number)
        except:
            return False
        if int(number) > 255 or int(number) < 0:
            return False
        if re.search(r"[a-zA-Z]", number):
            return False
        binary += bin(int(number))[2:].zfill(8)
    count=0
    for digit in binary:
        if digit == '0':
            if count < 9:
                return False
            if re.search(r"1", binary[count:]):
                return False
            return True
        count+=1
    return True