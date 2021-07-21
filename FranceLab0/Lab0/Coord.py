# Coord.py
# Kordel France
########################################################################################################################
# This file establishes a class for an object called Coord
########################################################################################################################


class Coord():
    def __init__(self, x, y):
        """
        Object class that represents a 2D-coordinate on a cartesian coordinate plane.
        Also referred to as a point throughout the code..
        :param x: the x-coordinate of the point on a cartesian coordinate plane
        :param y: the y-coordinate of the point on a cartesian coordinate plane
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Resets the point back to the origin..
        """
        self.x = 0.0
        self.y = 0.0


    def print_coord(self) -> str:
        """
        Prints or writes the coordinate in an aesthetic manner.
        :returns s: a string of the coordinate.
        """
        s = f'\tpoint: x-value = {self.x}, y-value = {self.y}'
        return s

