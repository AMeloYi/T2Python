from multiprocessing import Process
import time

def print_time(processName):
    result = 0
    while result < 100000:
        result += 20
        print("%s : %d" %(processName, result))




if __name__ == '__main__':
    # Create two threads as follows
    p1 = Process(target=print_time, args=('Thread-1',))
    p2 = Process(target=print_time, args=('Thread-2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
