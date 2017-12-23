class Dot:

    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y


class Circle(Dot):
    def __init__(self, radius, x0, y0):
        super().__init__(self, self.coordinate_x, self.coordinate_y)
        self.radius = radius
        self.center_coordinate_x = x0
        self.center_coordinate_y = y0

    def is_in(self):
        equation = ((self.coordinate_x - self.center_coordinate_x)**2 + (self.coordinate_y - self.center_coordinate_y)**2)
        if equation <= self.radius**2:
            return True
        else:
            return False


