class Point:
    # class level attribute
    default_color = "red"

    def __init__(self, x, y):
        # instance attribute
        self.x, self.y = x, y

    # decorator
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
p = Point(1, 2)
p2 = Point(1, 2)
print(p == p2)
    

# attributes dont have to be defined by constructor
p.z = 10

# both are valid
print(p.default_color)
print(Point.default_color)

# factory method - creates a new object
point = Point.zero()
print(point.x)

