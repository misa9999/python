# import re


# def is_float(val):
#     if isinstance(val, float):
#         return True
#     if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
#         return True

#     return False


# def is_int(val):
#     if isinstance(val, int):
#         return True
#     if re.search(r'^\-{,1}[0-9]+$', val):
#         return True

#     return False


# def is_number(val):
#     return is_int(val) or is_float(val)


n1 = input('n1: ')
n2 = input('n2: ')

try:
    n1 = float(n1)
    n2 = float(n2)

    print(n1 + n2)
except:
    print('error')
