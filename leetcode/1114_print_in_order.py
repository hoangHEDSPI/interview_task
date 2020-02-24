from threading import Lock

class Foo:
    def __init__(self):
        self.lock_1 = Lock()
        self.lock_2 = Lock()
        self.lock_1.acquire()
        self.lock_2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock_1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock_1:
            printSecond()
            self.lock_2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove thisline.
        with self.lock_2:
            printThird()
