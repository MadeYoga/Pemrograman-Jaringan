from threading import Thread

def print_message(message):
    count = 0
    while True:
        print(message)
        count +=1
        if count == 10:
            break

t1 = Thread(target=print_message, args=("aa",))
t2 = Thread(target=print_message, args=("bb",))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")
