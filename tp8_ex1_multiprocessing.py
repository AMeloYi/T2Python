from multiprocessing import Process
import time

def print_time(_processName):
    result = 0
    while result < 100000:
        result += 20
        print("%s : %d" %(processName, result))

# Create two threads as follows
try:
    _thread.start_new_thread(print_time, ("Thread-1", ))
    _thread.start_new_thread(print_time, ("Thread-2", ))
except:
    print("Error: unable to start thread")

while 1:
    pass