from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class People:
    name: str
    last_name: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f"Invalid type {type(self.name).__name__} != str in {self}")

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"


p1 = People("A", "5")
p2 = People("C", "3")
p3 = People("D", "4")
p4 = People("B", "6")

peoples = [p1, p2, p3, p4]
print(sorted(peoples, key=lambda people: people.last_name, reverse=True))

# print(p1.name)
# print(p1.last_name)
# print(p1.full_name)

print()
print(asdict(p1))
print(astuple(p2))
