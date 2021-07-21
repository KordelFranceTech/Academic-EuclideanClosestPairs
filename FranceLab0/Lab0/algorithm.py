# algorithm.py
# Kordel France
########################################################################################################################
# This file contains the algorithms and helper methods for the algorithms used to facilitate the closest pairs calculations
########################################################################################################################


import Lab0.helpers
from Lab0.Coord2Coord import Coord2Coord
import math


# good ol' vanilla merge_sort
def merge_sort(coord_list):
    """
    A sorting algorithm that sorts a list of data in O(n lg n) runtime through a divide-and-conquer strategy.
    :param coord_list: a list of points, or ordered pairs, unsorted and expressed as a list of Coord objects.
    :returns coord_list:  a list of points, or ordered pairs, sorted and expressed as a list of Coord objects.
    """
    if len(coord_list) > 1:
        mid = len(coord_list) // 2
        left_list = coord_list[:mid]
        right_list = coord_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        index_0 = 0
        index_1 = 0
        index_2 = 0

        while index_0 < len(left_list) and index_1 < len(right_list):
            left_coord = left_list[index_0]
            right_coord = right_list[index_1]

            if left_coord.y < right_coord.y:
                coord_list[index_2] = left_list[index_0]
                index_0 += 1
            else:
                coord_list[index_2] = right_list[index_1]
                index_1 += 1
            index_2 += 1

            while index_0 < len(left_list):
                coord_list[index_2] = left_coord
                index_0 += 1
                index_2 += 1

            while index_1 < len(right_list):
                coord_list[index_2] = right_coord
                index_1 += 1
                index_2 += 1
    return coord_list


def get_distance_between_pairs(pair0, pair1) -> float:
    """
    Computes the Euclidean distance between two points, or two ordered pairs, and returns the value of that distance.
    :param pair0: an ordered pair expressed as a Coord object.
    :param pair1: an ordered pair expressed as a Coord object.
    :returns float: a value representing the Euclidean distance between the two orderd pairs..
    """
    x0 = float(pair0.x)
    y0 = float(pair0.y)
    x1 = float(pair1.x)
    y1 = float(pair1.y)
    distance = (((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5

    # increase the global operation counter by 1 to visualize runtime costs later
    Lab0.helpers.op_count += 1
    Lab0.helpers.coord2coord_list.append(Coord2Coord(pair0, pair1, distance))
    return distance


def brute_force_algorithm(ordered_pairs) -> float:
    """
    A brute-force algorithm that gets the distance between each possible combination of points within a series of points.
    Runtime cost = O(n^2)
    :param ordered_pairs: a list of points, or ordered pairs, expressed as a list of Coord objects.
    :returns float: a value representing the smallest Euclidean distance between found between all of the
     points within the orderd_pairs series of points.
    """
    global min_distance
    # initialize a minimum distance for comparison
    min_distance = 100000000.0
    for index in range(0, len(ordered_pairs)):
        for subindex in range(0, len(ordered_pairs)):
            # we don't want to check a coordinate with itself, so skip it
            # we still count this as part of the O(n^2) runtime though
            if index != subindex:
                distance = get_distance_between_pairs(ordered_pairs[index], ordered_pairs[subindex])
                # this distance was smaller than the global min_distance
                if distance < min_distance:
                    min_distance = distance
    return min_distance


def find_closest_distance(num_coords, coord_list_0, coord_list_1):
    """
    A helper function that aids the divide-and-conquer algorithm.
    The function is a recursive method that continuously divides the two coord_list objects and checks for the minimum
    distance among all points, or ordered pairs, between the two coord_lists
    :param num_coords: an integer that expresses the number of coordinates in the entire array / list.
    :param coord_list_0: the left coord_list that resulted from the `divide` operation.
    :param coord_list_1: the right coord_list that resulted from the `divide` operation.
    """
    # if the length of the array is too small, just use the brute force method
    if num_coords <= 3:
        return brute_force_algorithm(coord_list_0)

    # find the midpoint, the division point of the array
    center = num_coords // 2
    center_coord = coord_list_0[center]

    # initialize two lists to populate from the original list
    left_list = []
    right_list = []

    for index in range(0, center):
        left_list.append(coord_list_0[index])

    for index in range(center, len(coord_list_0)):
        right_list.append(coord_list_0[index])

    # the smallest observed Euclidean distance value from the left list
    delta_left = find_closest_distance(center, left_list, coord_list_1)
    # the smallest observed Euclidean distance value from the right list
    delta_right = find_closest_distance(num_coords - center, right_list, coord_list_1)

    # the smallest observed Euclidean distance value between the left and right lists
    global delta_min
    if delta_left < delta_right:
        delta_min = delta_left
    else:
        delta_min = delta_right

    # we've found the local minimum, now initialize two sublists of coordinate objects
    # these lists are used to find the smallest distance between two points ACROSS the left and right halves
    # the preceding operation established the smallest distance between two points WITHIN the two halves separately
    coord_sublist_0 = []
    coord_sublist_1 = []

    # consolidate the left and right halves back together
    coord_list = left_list + right_list
    for index in range(0, num_coords):
        if abs(coord_list[index].x - center_coord.x) < delta_min:
            coord_sublist_0.append(coord_list[index])
        if abs(coord_list_1[index].x - center_coord.x) < delta_min:
            coord_sublist_1.append(coord_list_1[index])

    # we need to ensure the list is sorted in order for this to work
    # sort using merge_sort
    coord_sublist_0.sort(key=lambda coord: coord.y)
    # coord_sublist_0 = merge_sort(coord_sublist_0)

    # add n lg n operations to the operations counter to account for the cost of sorting
    Lab0.helpers.sort_count += (num_coords * math.log2(num_coords))

    # init global min distance of the left array
    global min_dist_left
    min_dist_left = delta_min

    # find the global min distance of the left array
    for index in range(0, len(coord_sublist_0)):
        sub_index = index + 1
        while sub_index < len(coord_sublist_0) and (coord_sublist_0[sub_index].y - coord_sublist_0[index].y) < min_dist_left:
            coord0 = coord_sublist_0[index]
            coord1 = coord_sublist_0[sub_index]
            min_dist_left = get_distance_between_pairs(coord0, coord1)
            sub_index += 1

    # init global min distance of the right array
    global min_dist_right
    min_dist_right = delta_min

    # find the global min distance of the right array
    for index in range(0, len(coord_sublist_1)):
        sub_index = index + 1
        while sub_index < len(coord_sublist_1) and (coord_sublist_1[sub_index].y - coord_sublist_1[index].y) < min_dist_right:
            coord0 = coord_sublist_1[index]
            coord1 = coord_sublist_1[sub_index]
            min_dist_right = get_distance_between_pairs(coord0, coord1)
            sub_index += 1

    # the minimum value between the two min distances from each half
    if min_dist_left < min_dist_right:
        return min_dist_left
    else:
        return min_dist_right


def divide_and_conquer_algorithm(num_coords, coord_list_0):
    """
    The 'efficient' algorithm with better runtime costs than the brute-force method.
    This algorithm facilitates a 'divide-and-conquer' strategy similar to merge sort and binary search.
    :param num_coords: the number of datapoints within the coord_list_0 coordinate array.
    :param coord_list_0: a list of points, or ordered pairs, expressed as a list of Coord objects.
    :returns float: a value representing the smallest Euclidean distance between found between all of the
     points within the coord_list0 series of points.
    """

    # we need to ensure the list is sorted in order for this to work
    # sort using merge_sort
    coord_list_0.sort(key=lambda coord: coord.x)
    # coord_list_0 = merge_sort(coord_list_0)

    # add n lg n operations to the operations counter to account for the cost of sorting
    Lab0.helpers.sort_count += (num_coords * math.log2(num_coords))

    coord_list_1 = []
    for index in range(0, len(coord_list_0)):
        coord_list_1.append(coord_list_0[index])

    # we need to ensure the list is sorted in order for this to work
    # sort using merge_sort
    coord_list_1.sort(key=lambda coord: coord.y)
    # coord_list_1 = merge_sort(coord_list_1)

    # add n lg n operations to the operations counter to account for the cost of sorting
    Lab0.helpers.sort_count += (num_coords * math.log2(num_coords))

    return find_closest_distance(num_coords, coord_list_0, coord_list_1)


# Note that this function is not called at runtime and is only used for debugging
def compare_sorting_algorithms(num_coords, coord_list_0):
    """
    A debugging algorithm built to verify that the custom merge-sort method provided the same results as Python3's
    built-in '.sort' method.
    :param num_coords: the number of datapoints within the coord_list_0 coordinate array.
    :param coord_list_0: a list of points, or ordered pairs, unsorted and expressed as a list of Coord objects.
    :returns coord_list:  a list of points, or ordered pairs, sorted and expressed as a list of Coord objects.
    """
    coord_list_0.sort(key=lambda coord: coord.x)
    coord_list_1 = []
    for index in range(0, len(coord_list_0)):
        coord_list_1.append(coord_list_0[index])


    print('\n\n\t\tMERGE SORT:')
    c = coord_list_1
    d = merge_sort(c)
    for i in range(0, len(d)):
        d[i].print_coord()

    print('\n\n\t\tREGULAR SORT:')
    coord_list_1.sort(key=lambda coord: coord.y)
    for i in range(0, len(coord_list_1)):
        coord_list_1[i].print_coord()
    return find_closest_distance(num_coords, coord_list_0, coord_list_1)

