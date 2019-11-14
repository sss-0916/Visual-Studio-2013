from multiprocessing import Process, Value
import time

def producer(memWrite):
    num = 1
    while True:
        print("memWrite!")
        memWrite.value = num
        num = num + 1

def consumer(memRead):
    while True:
        print("memRead: %d" % memRead.value)
        time.sleep(1)

if __name__ == "__main__":
    shareMem = Value('i', 0)

    test1 = Process(target = producer, args = (shareMem, ))
    test1.start()

    test2 = Process(target = consumer, args = (shareMem, ))
    test2.start()