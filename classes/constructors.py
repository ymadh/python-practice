class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

p = Point(1, 2)
p.draw()
