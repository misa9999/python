class WrongError(Exception):
    pass


def foo():
    raise WrongError("ERROR")


try:
    foo()
except WrongError as e:
    print(f"Error: {e}")
