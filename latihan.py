import random

rand = random.randint(0, 100)
print("random number: " + str(rand))

def isDigit(val):
    try:
        int(val)
        return True
    except:
        return False

while True:
    val = input('Enter number(0 - 99): ')
    if isDigit(val):
        val = int(val)
        if val == rand:
            print("Benar!")
            break
        elif val < rand:
            print("Too Low!")
        else:
            print("Too High!")
    else:
        print("invalid input")
