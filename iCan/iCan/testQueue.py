from multiprocessing import Process, Queue
import time

def producer(q_production):
    num = 1
    while True:
        print("q_production")
        try:
            q_production.put_nowait(num)
        except:
            pass

        num = num + 1

def consumer(q_consume):
    while True:
        try:
            num = q_consume.get_nowait()
        except:
            num = 0
            pass

        print("q_consume: %d" % num)
        time.sleep(1)

if __name__ == "__main__":
    q = Queue(10)

    test1 = Process(target = producer, args = (q, ))
    test1.start()

    test2 = Process(target = consumer, args = (q, ))
    test2.start()