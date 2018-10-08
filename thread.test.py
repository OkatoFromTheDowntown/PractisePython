import time
# thread is not recommendent in Python 3.x
# import _thread as thread
import threading

GLOBAL_VALUE = 1

# def print_time(user, delay):
#   count= 0
#   while count<5:
#     time.sleep(delay)
#     count +=1
#     global GLOBAL_VALUE
#     GLOBAL_VALUE += 1
#     print(user, time.ctime(time.time()), GLOBAL_VALUE)

# try:
#   thread.start_new_thread(print_time, ('Thread 1', 3))
#   thread.start_new_thread(print_time, ('Thread 2', 7))
#   thread.start_new_thread(print_time, ('THread 3', 9))
# except:
#   print('Error')

# while 1:
#   pass

threadLock = threading.RLock()


def print_time(threadName, delay, counter):
    print('Starting {0}'.format(threadName))
    while counter:
        # if exit: (threadName).exit()
        time.sleep(delay)
        print('{0}: {1}'.format(threadName, time.ctime(time.time())))
        counter -= 1
    else:
        print('Exiting {0}'.format(threadName))


class ThreadTask(threading.Thread):
    def __init__(self, threadID, name, counter):
        # threading.Thread.__init__(self)
        # super(ThreadTask, self).__init__()
        super().__init__()
        self.threadID, self.name, self.counter = threadID, name, counter

    def run(self):
        ''' run() will be executed while thread've been created '''
        # threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # threadLock.release()


threads = [ThreadTask(str(i), 'Thread-' + str(i), i) for i in range(1, 4)]

for thread in threads:
    thread.start()
else:
    for thread in threads:
        thread.join()

print('Exiting Main Thread.')
