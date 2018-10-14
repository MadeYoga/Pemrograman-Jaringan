import re

mail_input = input("input email ? ")

results = re.findall(r"(\w+)@([\w+\.-]+)", mail_input)

print (results)

if results == []:
    print("{} is not a valid mail".format(mail_input))
else:
    print("{} is a valid mail".format(mail_input))