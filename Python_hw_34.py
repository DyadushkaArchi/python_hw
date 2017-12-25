class CircleDot:

    def __init__(self, x, y, x0, y0, radius):
        self.coordinate_x = x
        self.coordinate_y = y
        self.center_coord_x = x0
        self.center_coord_y = y0
        self.radius = radius

    def is_in(self):
        equation = ((self.coordinate_x - self.center_coord_x) ** 2 + (self.coordinate_y - self.center_coord_y) ** 2)
        return equation <= (self.radius ** 2)

# (main.py)
#from Python_hw_34 import CircleDot
#CircleDot.__init__(CircleDot, 1, 1, 0, 0, 3)
#print(CircleDot.is_in(CircleDot))


