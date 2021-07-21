# helper.py
# Kordel France
########################################################################################################################
# This file contains helper methods for common utilities used throughout the app, including cost counters
########################################################################################################################

#characters that are acceptable as operands for the evaluation.
acceptable_chars = ['0','1','2','3','4','5','6','7','8','9','.']

# store number of operations of algorithms
brute_force_ops = []
efficient_ops = []
efficient_sort_ops = []

# global counters for number of operations for algorithms
op_count = 0
sort_count = 0

# helper methods for presenting points to user
global coord2coord_list
coord2coord_list = []


def sort_coord2coord_list():
    """
    Sorts a list of coordinates / points by distance betwen points.
    """
    for index in range(len(coord2coord_list) - 1, 0, -1):
        for subindex in range(index):
            if coord2coord_list[subindex].dist > coord2coord_list[subindex + 1].dist:
                temp = coord2coord_list[subindex]
                coord2coord_list[subindex] = coord2coord_list[subindex + 1]
                coord2coord_list[subindex + 1] = temp


def print_coord2coord_list(count):
    """
    Cleanly structures and prints a full list of coordinates / points to the console or writes to file.
    Prints the top n points with shortest distances as specified by count
    :param count: specifies the number of points to return
    """
    return_str = ''
    dist_list = []
    c = 0
    for index in range(0, len(coord2coord_list)):
        coord0 = coord2coord_list[index].coord0
        coord1 = coord2coord_list[index].coord1
        dist = coord2coord_list[index].dist
        if dist not in dist_list and c < count:
            c += 1
            return_str += f'\n{c}\tdistance {dist} from point ({coord0.x}, {coord0.y}) to point ({coord1.x}, {coord1.y})'
        dist_list.append(dist)
    return return_str


def remove_duplicates():
    """
    Removes duplicate coordinate pairs from the global coordinate list.
    For example, if we know the distance from A to B, we don't need the distance from B to A so remove it.
    """
    new_list = []
    global coord2coord_list
    global can_add
    for index in range(0, len(coord2coord_list)):
        can_add = True
        for subindex in range(index, len(coord2coord_list)):
            if coord2coord_list[index].coord0.x == coord2coord_list[subindex].coord1.x:
                if coord2coord_list[index].coord0.y == coord2coord_list[subindex].coord1.y:
                    can_add = False
        if can_add:
            new_list.append(coord2coord_list[index])
            coord0 = coord2coord_list[index].coord0
            coord1 = coord2coord_list[index].coord1
            dist = coord2coord_list[index].dist
            print(f'\n{index + 1}\tdistance {dist} from point ({coord0.x}, {coord0.y}) to point ({coord1.x}, {coord1.y})')
    coord2coord_list = new_list
