from time import sleep
from threading import Thread
from threading import Lock


class Tickets:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, amount):
        self.lock.acquire()

        if self.stock < amount:
            print("We don't have enough tickets")
            self.lock.release()
            return

        sleep(1)

        self.stock -= amount
        print(f"You bought {amount} tickets. Remaining tickets {self.stock}")

        self.lock.release()


if __name__ == "__main__":
    tickets = Tickets(10)

    threads = []

    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    execute = True
    while execute:
        execute = False

        for t in threads:
            if t.is_alive():
                execute = True
                break


# def xpto(text, time):
#     sleep(time)
#     print(text)


# t1 = Thread(target=xpto, args=("Thread 1", 10))
# t1.start()
# t1.join()

# while t1.is_alive():
#     print("waiting...")
#     sleep(2)


# print("Thread down")


# def xpto(text, time):
#     sleep(time)
#     print(text)


# t1 = Thread(target=xpto, args=("Thread 1", 5))
# t1.start()

# t2 = Thread(target=xpto, args=("thread 2", 2))
# t2.start()

# t3 = Thread(target=xpto, args=("thread 3", 3))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(0.5)


# class MyThread(Thread):
#     def __init__(self, text, time):
#         self.text = text
#         self.time = time

#         super().__init__()

#     def run(self):
#         sleep(self.time)
#         print(self.text)


# t1 = MyThread("Thread 1", 5)
# t1.start()

# t2 = MyThread("Thread 2", 3)
# t2.start()

# t3 = MyThread("Thread 3", 2)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)
