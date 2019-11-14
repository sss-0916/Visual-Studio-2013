from multiprocessing import Process

global_val = 0

#def fun1():
#    global global_val
#    global_val = 10

#def fun2():
#    print("global: %d" % global_val)

#fun1()
#fun2()

def func1():
    while True:
        print("global_val: %d" % global_val)

def func2():
    num = 1
    while True:
        global global_val
        global_val = num
        num = num + 1

if __name__ == "__main__":
    test1 = Process(target = func2)
    test1.start()

    test2 = Process(target = func1)
    test2.start()