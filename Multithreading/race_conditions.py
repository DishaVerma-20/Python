import threading 
import time

balance = 1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock: # ab 800 hogaa
        temp = balance # read
        time.sleep(0.0001)
        balance = temp - amount # write back

t1 = threading.Thread(target = withdraw, args=(100, ))
t2 = threading.Thread(target = withdraw, args = (100, ))
t1.start()
t2.start()
t1.join()
t2.join()

print("--Bank Transfer--")

print(f"Expected balance: 800 -> Got = {balance}") # 900 aayga, dono temp 1 saath run ho gaye, 1 saath minus vgera
# iske prevention ke liye we uses lock