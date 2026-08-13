import time
import threading

def task():
    print("This task is running")
    # 2 sec
    time.sleep(2)
    print("Task finished")


print("Main program start\n")
t = threading.Thread(target=task)
t.start()
print("Main program end\n")