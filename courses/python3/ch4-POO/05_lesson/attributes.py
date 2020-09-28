class A:
    var = 123

    def __init__(self):
        pass


a1 = A()
a2 = A()

A.var = 'new'

print(a1.var)
print(a2.var)
print(A.var)
