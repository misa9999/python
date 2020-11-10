from collections import deque
from time import sleep


queue = deque(maxlen=10)

for i in range(1000):
    queue.append(i)
    sleep(1)
    print(queue)

# queue.extend([1, 2, 3, 4])
# queue.append(5)
# queue.append(6)
# print(queue)


# queue.append("yuuki")
# queue.append("misa")
# queue.append("megumin")
# queue.append("lucy")

# print(f"{queue.popleft()} leave")
# print(f"{queue.popleft()} leave")
# print(f"{queue.popleft()} leave")
# print(f"{queue.popleft()} leave")


# class Books:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"successfully added [{book}]")

#     def remove_book(self):
#         rm = self.books.pop()
#         print(f"Removed [{rm}]")


# if __name__ == "__main__":
#     book = Books()
#     book.add_book("Book 1")
#     book.add_book("Book 2")
#     book.remove_book()
