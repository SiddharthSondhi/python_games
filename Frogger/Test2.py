from threading import Thread
def str_func(a):
    while True:
        print(a)

t1=Thread(target=str_func,args=('thread 1',))
t1.start()
str_func('mainthread')
