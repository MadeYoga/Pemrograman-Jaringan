import re

mail_input = input("masukan email? ")
results = re.findall(r"(\w+)@([\w+\.-]+)", mail_input)

print(results)

if results == []:
    print("email tidak valid")
else:
    print("email valid")
