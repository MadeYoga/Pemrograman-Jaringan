import threading

from threading import Lock

# race condition terjadi saat beberapa thread mengakses resource secara bersamaan 
# yang mengakibatkan nilai dari resource jadi tidak sesuai
# cara handlenya dengan menggunakan lock pada threading
# yaitu mengunci resource selama digunakan, semacam flag
# setelah selesai digunakan resource dilepas oleh thread1 dan dapat digunakan oleh thread lainnya

value = 0

def increment(delta_val, max, lock_resources=False):
    global value
    if lock_resources:
        lock.acquire()
        while value < max:
            value += delta_val
            print(value)
            if value > delta_val * 100:
                break
        lock.release()
    else:
        while value < max:
            value += delta_val
            print(value)
            if value > delta_val * 100:
                break
    
lock = Lock()

# lock, hasil output pasti sama
thread1 = threading.Thread(target=increment, args=(1, 100, True,)) # 1 - 100 increment += 1
thread2 = threading.Thread(target=increment, args=(2, 200, True,)) # 100 - 200 increment += 2
thread3 = threading.Thread(target=increment, args=(5, 500, True,)) # 200 - 500 increment += 5

# # increment berantakan, hasil output berbeda stiap kali run script
# thread1 = threading.Thread(target=increment, args=(1, 500,)) 
# thread2 = threading.Thread(target=increment, args=(2, 500,)) 
# thread3 = threading.Thread(target=increment, args=(5, 500,)) 

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("done")
