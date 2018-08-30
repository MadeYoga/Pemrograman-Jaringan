import re

mail = input("input email: ")

nrp = re.search(r'\d+', mail)
res_nrp = nrp.group()

domain = re.search(r'@.*', mail)
res_domain = domain.group()[1:]

# cara 2
res_mail = re.search(r"m(\d+)@([\w\.-]+)", mail)

print("NRP: " + res_nrp + "\nDOMAIN: " + res_domain)
print("res_mail : " + res_mail[1] + ", " + res_mail[2])

