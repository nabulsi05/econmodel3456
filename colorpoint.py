import random

from point import Point


class ColoredPoint(Point):
    COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "beige", "bordeaux", "marsala"]

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"That is an invalid color. Accepted colors are {self.COLORS}")

def __str__(self):
    return f"{self.color}({self.x}, {self.y})"

@classmethod
def add_extra_color(cls, color):
    cls.COLORS.append(color)

@property
def distance_origin(self):
    result = (self.x**2 + self.y**2)**0.5
    if result == int(result):
        return

p1 = ColoredPoint(10, 10, "red")

colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(ColoredPoint.COLORS)
                     )
    )

print(colored_points)

ColoredPoint.add_extra_color("orange")
p2 = ColoredPoint(5, 5, "orange")
print(p2)