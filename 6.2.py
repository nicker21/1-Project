


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, p):
        if ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) <= self.radius ** 2:
            return True
        else:
            return False


