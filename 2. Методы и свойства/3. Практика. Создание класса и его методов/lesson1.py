from __future__ import annotations


class Point:
    list_points: list = []

    def __init__(self, coord_x: int = 0, coord_y: int = 0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x: int, new_y: int) -> None:
        self.x = new_x
        self.y = new_y

    def go_home(self) -> None:
        self.move_to(0, 0)

    def calc_distance(self, another_point: Point) -> float:
        if not isinstance(another_point, Point):
            raise ValueError("Argument isn't Point class")

        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5

    def print_point(self) -> None:
        print(f'Point w/ coordinates ({self.x}, {self.y})')

    def __str__(self):
        return f'Point: ({self.x}, {self.y})'


p1 = Point(5, 6)
p3 = Point(77, -88)
p1.print_point()

p2 = Point(7, 8)
p2.print_point()

print(p2.calc_distance(p1))
print(p1.list_points)
