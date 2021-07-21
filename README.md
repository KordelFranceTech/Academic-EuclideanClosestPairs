# FranceLab 0 - Kordel K. France

This project was constructed for the Data Structures class, 605.621 section 83, at Johns Hopkins University. The project 
finds the closest pair or pairs of points within a series of points located on a 2D Cartesian coordinate system. The program was built for educational
purposes only.

The file `algorithm.py` contains the brute-force and efficient algorithms. In this file, the function
`divide_and_concquer_algorithm` is the efficient algorithm mentioned in the assignment handout.

## Running FranceLab0
1. **Ensure Python 3.7 is installed on your computer.**
2. **Navigate to the FranceLab0 directory.** For example, `cd User\Documents\PythonProjects\FranceLab0`.
Do NOT `cd` into the `Lab0` module.
3. **Run the program as a module: `python -m Lab0`.**
4. **Input and output files ar located in the `io_files` subdirectory.** 
In here, the input files contain `reqInput` in the name and the names are formatted as `reqInput{n}.txt` where `n` is the 
data count. Note that `reqInput25.txt` and `reqInput100.txt` are the files provided for the assignment via Blackboard. 
The other `reqInput` files contain data points that have been automatically generated for the purposes of larger trace runs.
Output files contain the name `traceRun` and the file names are formatted as `traceRun{n}_{type}.txt` where `n` represents 
the data count and `type` represents either a cost or correctness run. A log of the imported input, the resultant 
operations, and a duplication of the console output is located in each of these files. 

**Note: When the module is run, traceRuns will automatically regenerate for `n` = 6, 10, 25, 100, 200, and 200small.
You will see traceRuns for `n = 1000` in the `io_files` directory but these are provided for reference and will not
regenerate at runtime due to the time it takes to complete these trace runs. Additionally, note that the `200small` 
traceRuns are meant to test points whose coordinate values are contained within the range [0, 1] in order to address corner cases of the 
algorithms.**

### Lab0 Usage

```commandline
usage: python -m Lab0
```

### Project Layout

Here is how the project is structured and organized.

* `FranceLab2`: *The parent folder of the project. This should be the last subdirectory you navigate to to run the
project.*
    * `README.md`:
      *A guide on what the project does, how to run the project, etc.*
    * `io_files`:
      *A subdirectory containing all of the input and output `.txt` files.*
    * `Lab2`: This is the module of the entire program package. It is not a directory. Do not navigate into it.
      * `__init__.py`
        *As the name suggests, this file initializes the program and gives access to the file processing capabilities
        to other programs.*
      * `__main__.py` 
        *This file processes the I/O files, begins the general program, and facilitates the presentation of the final graph.*
      * `algorithm.py`
        *This file contains the algorithms and helper methods for the algorithms used to facilitate the closest pairs calculations.*
      * `config.py`
        *This file contains hyperparameters to control debugging features.*
      * `file_processing.py`
        *This file contains I/O methods for processing the input and output .txt files contained in the `io_files` directory.*
      * `Coord.py`
        *This file establishes a class for an object called Coord, which is a representation of a point on a 2D graph.*
      * `Coord2Coord.py`
        *This file establishes a class for an object called Coord2Coord, which is the Euclidean distance between 
        two Coord objects.*
      * `helpers.py`
        *This file contains helper methods for common utilities used throughout the app, including cost counters.*
      * `graph.py`
        *This file contains a function to graph and display algorithmic efficiency data.*
      * `genetic.py`
        *This file contains logic for a genetic algorithm that finds the closest point among a series of points.
        While the file is not used in the lab, a genetic algorithm was my first (and failed) approach of developing an 
        "efficient algorithm" as specified in the lab handout. I included it due to this and because I briefly mention it
        in the analysis document. If desired, the genetic algorithm may be run with the command `python Lab0/genetic.py`.*

###References
The following items were used as references for the construction of this project. 
1) Miller, B. N., & Ranum, D. L. (2014). Problem solving with algorithms and data structures using Python (2nd ed.). 
Decorah, IA: Brad Miller, David Ranum.
2) Cormen, T. H., & Leiserson, C. E. (2009). Introduction to Algorithms, 3rd edition. 
3) Merge Sort. GeeksforGeeks. (2021, June 20). https://www.geeksforgeeks.org/merge-sort/. 
4) QuickSort. GeeksforGeeks. (2021, June 20). https://www.geeksforgeeks.org/quick-sort/. 

