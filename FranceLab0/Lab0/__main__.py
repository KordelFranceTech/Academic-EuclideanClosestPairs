#__main__.py
#Kordel France
########################################################################################################################
#This file launches the Closest Pairs Program and sets up file processing.
########################################################################################################################

from Lab0.file_processing import build_correctness_run, build_trace_runs, build_trace_runs_small
from Lab0.graph import graph_runtime_data
from Lab0.helpers import brute_force_ops, efficient_ops, efficient_sort_ops

#print a header for UI aesthetics
#this same header is output to the file after the output file is specified by the user
print('*****************************************************************************************')
print('*****************************************************************************************')
print('*****************************************************************************************')
print('\t\t\t\tWelcome')
print('*****************************************************************************************')
print('*****************************************************************************************')

# build correctness and cost runs from Dr. Chlan's input files
build_correctness_run(in_file='reqInput6.txt', out_file='traceRun6.txt', n=6)
build_correctness_run(in_file='reqInput10.txt', out_file='traceRun10.txt', n=10)
build_correctness_run(in_file='reqInput25.txt', out_file='traceRun25.txt', n=25)
build_correctness_run(in_file='reqInput100.txt', out_file='traceRun100.txt', n=100)

# build correctness and cost runs from custom input files
count = 200
# build trace runs - this builds a file with n randomly generated 2d points
build_trace_runs(count=count)
build_correctness_run(in_file=f'reqInput{count}.txt', out_file=f'traceRun{count}.txt', n=count)
build_trace_runs_small(count=count)
build_correctness_run(in_file=f'reqInput{count}small.txt', out_file=f'traceRun{count}small.txt', n=count)

# graph the data
graph_runtime_data(brute_force_ops, efficient_ops, efficient_sort_ops)


