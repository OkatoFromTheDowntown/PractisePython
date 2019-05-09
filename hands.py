import threading

threadLock = threading.Lock()


class Hands(threading.Thread):
    def __init__(self, threadId, name, task):
        super().__init__()
        self.threadId = threadId
        self.name = name
        self.task = task

    def run(self):
        # threadLock.acquire()
        self.task()
        # threadLock.release()


def test():
    def dosomething(a='Hello World'):
        def dooo():
            print(a)
        return dooo

    hands = [Hands(str(i), 'Thread-' + str(i),
                   dosomething(**{'a': i})) for i in range(0, 4)]

    for hand in hands:
        hand.start()
    else:
        for hand in hands:
            hand.join()

    print('Exiting the main thread.')


if __name__ == "__main__":
    test()
