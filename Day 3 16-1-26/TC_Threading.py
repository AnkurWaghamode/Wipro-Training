import threading

def task():
    print("thread is running")

t1=threading.Thread(target=task)
t2=threading.Thread(target=task,aargs=("Thread2"))
t1.start()
t1.join()
t2.start()
t2.join()

print("main thread ends")
