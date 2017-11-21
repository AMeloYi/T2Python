import _thread
import time

def print_time(threadName):
    result = 0
    while result < 500000:
        result += 20
        print("%s : %d" %(threadName, result))


if __name__ == '__main__':
    # Create two threads as follows
    _thread.start_new_thread(print_time, ("Thread-1", ))
    _thread.start_new_thread(print_time, ("Thread-2", ))
    time.sleep(10)
