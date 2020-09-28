from time import time
from time import sleep


def speed(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        time_ = (end_time - start_time) * 1000
        print(f'\nThe function {func.__name__} took {time_:.2f}ms to execute')
        return result
    return inner

@speed
def delay():
    for i in range(100):
        print(i, end='')


delay()

# def master(func):
#     def slave(*args, **kwargs):
#         print('...')
#         func(*args, **kwargs)
#     return slave

# @master
# def say_hi():
#     print('hi')

# @master
# def other_func(msg):
#     print(msg)


# other_func('Yahallo')
# say_hi()

# say_hi = master(say_hi)

# def say_hi():
#     print('Hi')


# variable = say_hi
# variable()