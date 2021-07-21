# file_processing.py
# Kordel France
########################################################################################################################
# This file contains functions that perform I/O file processing of the input and output files.
########################################################################################################################

from Lab0.Coord import Coord
from Lab0.config import DEBUG_MODE
from Lab0.algorithm import brute_force_algorithm, divide_and_conquer_algorithm
import Lab0.helpers
import math
import time
import random


def process_file_data(input_text_file, output_text_file):
    """
    Takes an input file to read data from line by line, character by character, and formats the data into Coord objects.
    :param input_text_file: the text file to read data in from.
    :param output_text_file: the text file to write corresponding trace run output to.
    ;return coord_list: a list of 2D coordinate points as Coord objects
    ;return output_string: a string containing all of the trace run detail that can be printed to the console or
    written to the output file
    """
    output_string = ''
    output_string += 'Checking input file for errors...'
    input_file = open(str(input_text_file), 'r')
    global can_add_x
    global can_add_y
    global expr_count
    global line_count
    can_add_x = False
    can_add_y = False
    expr_count = 0
    line_count = 0
    # read the entire file once and count the characters to know how large a CharStack should be initalized for
    while 1:
        single_char = input_file.read(1)
        if not single_char:
            can_add_y = True
            line_count += 1
            if can_add_x and can_add_y:
                expr_count += 1
                can_add_x = False
                can_add_y = False
            break
        elif str(single_char) == ' ':
            can_add_x = True
            expr_count += 1
            continue
        elif single_char == '\n':
            can_add_y = True
            line_count += 1
            if can_add_x and can_add_y:
                expr_count += 1
                can_add_x = False
                can_add_y = False
            continue
    time.sleep(1.0)

    # if any errors were found, notify the user
    if 2 * line_count == expr_count:
        output_string += 'Found no errors in input file. Forming points...'
    # otherwise, write the data to the output file, print the details to the screen and continue
    else:
        error_count = (2 * line_count) - expr_count
        output_text_file = open(str(output_text_file), 'a')
        output_string += f'\nFound {expr_count} values over {line_count} lines.'
        output_string += f'\nYou need an x- and y-coordinate on each line to form a point.'
        output_string += f'\nForming points for {expr_count} values. Neglecting {error_count} errors...'
        output_text_file.close()

    # a bit of defensive programming and likely not needed: close and reopen file just to ensure we read exact same data as before
    input_file.close()
    input_file = open(str(input_text_file), 'r')
    global coord_list
    global curr_readin_val
    global curr_x_val
    coord_list = []
    curr_readin_val = ''
    curr_x_val = 0.0
    last_char = ''

    # read the entire file again, this time actually reading data in to the CharStack for use
    # clean the data as it is read
    while 1:
        if DEBUG_MODE:
            print(curr_readin_val)
        single_char = input_file.read(1)
        if not single_char:
            x = curr_x_val
            y = float(curr_readin_val)
            new_coord = Coord(x, y)
            coord_list.append(new_coord)
            if DEBUG_MODE:
                print(f'found y-value: {curr_readin_val}')
                print(f'new coord appended: {new_coord.print_coord()}')
            curr_readin_val = ''
            break
        elif str(single_char) == ' ':
            if DEBUG_MODE:
                print(f'found x-value: {curr_readin_val}')
            curr_x_val = float(curr_readin_val)
            curr_readin_val = ''
        elif single_char == '\n' or last_char == '\n':
            x = curr_x_val
            y = float(curr_readin_val)
            new_coord = Coord(x, y)
            coord_list.append(new_coord)
            if DEBUG_MODE:
                print(f'found y-value: {curr_readin_val}')
                print(f'new coord appended: {new_coord.print_coord()}')
            curr_readin_val = ''
            continue
        else:
            curr_readin_val += single_char
        last_char = single_char
    input_file.close()


    output_string += f'\nsucessfully read in {2 * len(coord_list)} values and {len(coord_list)} points'
    output_string = ''
    for coord in coord_list:
        s = coord.print_coord()
        output_string += f'\n{s}'
    return coord_list, output_string


def build_correctness_run(in_file, out_file, n):
    """
    Builds an output file from the input file that acts as a correctness run to verify the output matches the input
    and checks for algorithm correctness.
    :param in_file: the name of the text file to read data in from.
    :param out_file: the name of the text file to write corresponding trace run output to.
    ;param n: an integer that dictates how large the trace run data set is.
    """
    out_file = out_file[:-4] + '_correctness.txt'
    output_string = ''
    cost_string = ''

    output_string += f'\n\n\n\n\tCORRECTNESS RUN FOR N = {n}'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'

    #begin processing the data in the input file and format it for conversion of all prefix expressions
    input_file = f'io_files/{in_file}'
    output_file = f'io_files/{out_file}'
    coord_list, trace_string = process_file_data(input_file, output_file)
    num_coords = len(coord_list)

    brute_force_dist = brute_force_algorithm(coord_list)
    output_string += f'\n\tClosest distance with brute-force algorithm: {brute_force_dist}'
    cost_string += f'\n\tCost for brute-force algorithm with input size {n}:\t\t\t{int(Lab0.helpers.op_count) + int(n)}'
    cost_string += f'\n\t\tExpected cost: {int(n) ** 2}'

    Lab0.helpers.brute_force_ops.append(Lab0.helpers.op_count)
    Lab0.helpers.op_count = 0
    Lab0.helpers.sort_count = 0
    Lab0.helpers.coord2coord_list = []
    div_and_con_dist = divide_and_conquer_algorithm(num_coords, coord_list)
    Lab0.helpers.sort_coord2coord_list()

    output_string += f'\n\tClosest distance with divide-and-conquer algorithm: {div_and_con_dist}'
    cost_string += f'\n\tCost for divide-and-conquer algorithm with input size {n}:\t\t{Lab0.helpers.op_count}' \
                   f' (not including sorting)'
    cost_string += f'\n\tCost for divide-and-conquer algorithm with input size {n}:' \
                   f'\t\t{int(Lab0.helpers.op_count + Lab0.helpers.sort_count)} (including sorting)'
    cost_string += f'\n\t\tExpected cost: {int(int(n) * math.log2(int(n)))}'
    Lab0.helpers.efficient_ops.append(Lab0.helpers.op_count)
    Lab0.helpers.efficient_sort_ops.append(int(Lab0.helpers.sort_count + Lab0.helpers.op_count))

    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += f'\n\nTop 3 ordered closest pairs sorted via merge sort:{Lab0.helpers.print_coord2coord_list(count=3)}'
    output_string += f'\n\nTop 5 ordered closest pairs sorted via merge sort:{Lab0.helpers.print_coord2coord_list(count=5)}'
    output_string += f'\n\nInput Data:{trace_string}'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'
    print(output_string)
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(output_string)
    output_text_file.close()

    Lab0.helpers.op_count = 0
    Lab0.helpers.sort_count = 0
    time.sleep(1.5)
    build_cost_run(in_file, out_file, n, trace_string, cost_string)
    time.sleep(1.5)



def build_cost_run(in_file, out_file, n, trace_string, cost_string):
    """
    Builds an output file from the input file that acts as a cost run to compute and write the expected and actual values
    of runtime costs for the brute-force and divide-and-conquer algorithms.
    :param in_file: the name of the text file to read data in from.
    :param out_file: the name of the text file to write corresponding trace run output to.
    ;param n: an integer that dictates how large the trace run data set is.
    ;param trace_string: a string that contains the input data received from the correctness run.
    ;param cost_string: a string that contains the runtime cost data for each algorithm.
    """
    out_file = out_file[:-15] + 'cost.txt'
    output_string = ''
    output_string += f'\n\n\tCOST RUN FOR N = {n}'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += cost_string
    output_string += '\n-----------------------------------------------------------------------------------------'
    output_string += f'\n\nInput Data:{trace_string}'
    output_string += '\n*****************************************************************************************'
    output_string += '\n*****************************************************************************************'
    output_string += '\n*****************************************************************************************'

    #begin processing the data in the input file and format it for conversion of all prefix expressions
    input_file = f'io_files/{in_file}'
    output_file = f'io_files/{out_file}'
    print(output_string)
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(output_string)
    output_text_file.close()
    coord_list = process_file_data(input_file, output_file)



def build_trace_runs(count) -> [Coord]:
    """
    Builds an input file of pseudo-randomly generated data that can be converted to 2D coordinate points and used for
    trace runs.
    :param count: an integer that dictates how large the trace run data set is.
    :returns [Coord]: a list of points in the form of Coord objects to be used for computation.
    """
    coord_list = []
    for index in range(0, count):
        x_coord = random.uniform(0, 10000)
        y_coord = random.uniform(0, 10000)
        coord = Coord(x_coord, y_coord)
        coord_list.append(coord)
    output_file = f'io_files/reqInput{count}.txt'
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    for index in range(0, len(coord_list)):
        output_text_file.write(f'{coord_list[index].x} {coord_list[index].y}')
        if index != len(coord_list) - 1:
            output_text_file.write('\n')
    output_text_file.close()
    return coord_list


def build_trace_runs_small(count) -> [Coord]:
    """
    Builds an input file of pseudo-randomly generated data that can be converted to 2D coordinate points and used for
    trace runs.
    The difference between this function and the function `build_trace_runs` is that this function is meant to test
    corner cases with small numbers so only values contained within the interval [0, 1] are generated here.
    :param count: an integer that dictates how large the trace run data set is.
    :returns [Coord]: a list of points in the form of Coord objects to be used for computation.
    """
    coord_list = []
    for index in range(0, count):
        x_coord = random.uniform(0, 1)
        y_coord = random.uniform(0, 1)
        coord = Coord(x_coord, y_coord)
        coord_list.append(coord)
    output_file = f'io_files/reqInput{count}small.txt'
    output_text_file = open(str(output_file), 'a')
    output_text_file.truncate(0)
    for index in range(0, len(coord_list)):
        output_text_file.write(f'{coord_list[index].x} {coord_list[index].y}')
        if index != len(coord_list) - 1:
            output_text_file.write('\n')
    output_text_file.close()
    return coord_list

