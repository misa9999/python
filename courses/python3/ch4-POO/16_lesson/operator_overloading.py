class Retangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Retangle(new_x, new_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"<class> 'Retangle({self.x}, {self.y})'"


r1 = Retangle(10, 20)
r2 = Retangle(10, 20)
r3 = r1 + r2
print(r1 == r3)
