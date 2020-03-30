import threading
import datetime

def f():
    for i in range(1, 10):
        print(i)
        print(datetime.datetime.now())

thread = threading.Thread(target=f)
thread.start()

print("This may print while the thread is running.")
thread.join()
print("This will always print after the thread has finished.")

