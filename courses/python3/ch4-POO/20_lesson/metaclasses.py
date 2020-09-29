# class Father:
#     name = "Test"


# A = type("A", (Father,), {"attr": "Hello world"})

# a = A()
# print(a.name)


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if "attr_class" in namespace:
            del namespace["attr_class"]
            # if "b_speak" not in namespace:
            #     print(f"you need to create the method b_speak in {name}")
            # else:
            #     if not callable(namespace["b_speak"]):
            #         print(f"b_speak needs to be a method, not an attribute in {name}")

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_class = "Value A"


class B(A):
    attr_class = "Value A"


class C(B):
    attr_class = "Value C"


c = C()
print(c.attr_class)
# class A(metaclass=Meta):
#     def speak(self):
#         self.b_speak()


# class B(A):
#     test = "Value"

#     def b_speak(self):
#         print("HI")

#     def xpto(self):
#         pass
