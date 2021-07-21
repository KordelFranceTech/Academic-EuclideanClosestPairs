# Coord2Coord.py
# Kordel France
########################################################################################################################
# This file establishes a class for an object called Coord2Coord, which is the Euclidean distance between  two Coord objects.
########################################################################################################################


from Lab0 import Coord


class Coord2Coord():
    def __init__(self, coord0, coord1, dist):
        """
        Object class that represents a line between two points (coordinates) in 2d Cartesian coordinate space.
        :param coord0: a Coord coordinate object that constitutes the first end of a line on a plane
        :param coord1: a Coord coordinate object that constitutes the last end of a line on a plane
        :param dist: the physical distance between coord0 and coord1 in 2d space
        """
        self.coord0 = coord0
        self.coord1 = coord1
        self.dist = dist


    def print_coord2coord(self):
        """
        Prints or writes the two coordinate points and the distance between them in an aesthetic manner.
        """
        print(f'\tdistance: {self.dist}')
        print(f'first coord: ({self.coord0.x}, {self.coord0.y})'
              f'\nsecond coord: ({self.coord1.x}, {self.coord1.y}')


