"""
diameter = 2R
R = diameter / 2
Circumference = pi x diameter
Area = pi x R x R
Area of sector = (angle /  360) x pi x R x R
"""


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        C = self.__pi * self.diameter
        return C

    def calculate_area(self):
        r = self.diameter / 2
        area = self.__pi * r * r
        return area

    def calculate_area_of_sector(self, angle):
        r = self.diameter / 2
        area_of_sector = (angle / 360) * self.__pi * r * r
        return area_of_sector


