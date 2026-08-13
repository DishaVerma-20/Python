import time
import threading

def task(name):
    print(f"{name} task is running\n")
    time.sleep(2)
    print(f"{name} task is finished\n")

print("Main program starts")
t1 = threading.Thread(target = task, args = ("cooking", )) # tuple hai toh comma
t2 = threading.Thread(target = task, args = ("baking", ))
t1.start()
t2.start()
t1.join() # jbtk t1 khtm nahi hota
t2.join() # jbtk t2 khtm nahi hota neeche nahi jaana hai
print("Main program end\n")
