class Point:
    def set_coordinates(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
            print('Got not Point')
        else:
            print(((another_point.x - self.x) ** 2 + (another_point.y - self.y) ** 2) ** 0.5)


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
p1.get_distance(p2)
p1.get_distance(10)
