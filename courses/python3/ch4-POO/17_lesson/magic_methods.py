class A:
    # def __new__(cls, *args, **kwargs):
    # return super().__new__(cls)
    # cls.name = "Misa Amane"

    # def hello(*args, **kwargs):
    #     print("Say HI")

    # cls.hello = hello

    # if not hasattr(cls, "_exist"):
    #     cls._exist = object.__new__(cls)

    # return cls._exist

    def __init__(self):
        print("dunder INIT")

    def __call__(self, *args, **kwargs):
        result = 1

        for i in args:
            result *= i

        return result

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __del__(self):
        # print("dunder DEL")
        pass

    def __str__(self):
        return "dunder STR"

    def __len__(self):
        return 55


a = A()
print(len(a))
