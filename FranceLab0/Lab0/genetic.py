# genetic.py
# Kordel France
########################################################################################################################
# This file contains logic for a genetic algorithm that finds the closest point among a series of points.
# While the file is not used in the lab, a genetic algorithm was my first (and failed) appraoch of developing an
#       "efficient" algorithm as specified in the lab handout. I included it due to this and because I briefly mention it
#       in the analysis document.
########################################################################################################################

import random
import matplotlib.pyplot as plt
import numpy as np


#HYPERPARAMETERS
#######################################################
GENERATIONS = 100
POPULATION_SIZE = 1000
SHOULD_GRAPH = False
MIN_X = -1000
MIN_Y = -1000
MAX_X = 1000
MAX_Y = 1000
MUTATION_INTERVAL = 0.05


#FUNCTION DEFINITIONS
#######################################################
#set initial population
def generatePopulation(size, xBoundaries, yBoundaries):
    lowerXboundary, upperXboundary = xBoundaries
    lowerYboundary, upperYboundary = yBoundaries
    population = []
    for i in range(size):
        individual = {
            "x0": random.uniform(lowerXboundary, upperXboundary),
            "y0": random.uniform(lowerYboundary, upperYboundary),
            "x1": random.uniform(lowerXboundary, upperXboundary),
            "y1": random.uniform(lowerYboundary, upperYboundary),
        }
        population.append(individual)
    return population


#this is the function we test each individual/solution's fitness with
#consider performing a genetic algorithm on NN hyperparameters
def applyFunction(individual):
    x0 = individual["x0"]
    y0 = individual["y0"]
    x1 = individual["x1"]
    y1 = individual["y1"]
    return (((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5
    # return math.sin(math.sqrt(x ** 2 + y ** 2))
    # return (3 * math.sin(4 * x)) + (4 * math.cos(3 * x))


#fitness calculation
#may be worthwhile to set a fitness threhsold and only mutate candidates below this fitness threshold
#may be worthwhile to also only mutate candidates randomly, or combo of this and ^
#this way, we mutate only unfit solutions instead of fit solutions
def choiceByRoulette(sortedPopulation, fitnessSum):
    offset = 0
    normalizedFitnessSum = fitnessSum
    lowestFitness = applyFunction(sortedPopulation[0])
    if lowestFitness < 0:
        offset = -lowestFitness
        normalizedFitnessSum += offset * len(sortedPopulation)
    draw = random.uniform(0, 1)
    accumulated = 0
    for individual in sortedPopulation:
        fitness = applyFunction(individual) + offset
        probability = fitness / normalizedFitnessSum
        accumulated += probability
        if draw <= accumulated:
            return individual


#we only want the fittest candidates/solutions
def sortPopulationByFitness(population):
    return sorted(population, key=applyFunction)


#if crossover is not implemented, we are just making copies of old generations
#there would be no new candidates/individuals
#crossover has to be implemented
def crossover(individualA, individualB):
    x0a = individualA["x0"]
    y0a = individualA["y0"]
    x0b = individualB["x0"]
    y0b = individualB["y0"]
    x1a = individualA["x1"]
    y1a = individualA["y1"]
    x1b = individualB["x1"]
    y1b = individualB["y1"]
    #take first parts of gene a and swap with gene b
    #important to note that crossover is replacement, not addition
    #new candidates are added to the population through crossover, and the pre-crossover candidates removed
    #may be worthwhile to apply a "crossover function" that experiments with different crossover patterns and follows
    ###a certain function/threshold
    # return {"x": (xa + xb) / 2, "y": (ya + yb) / 2}
    return {"x0": (x0a + x0b) / 2, "y0": (y0a + y0b) / 2, "x1": (x1a + x1b) / 2, "y1": (y1a + y1b) / 2}


#if mutation is not implemented, we are not bringing in new randomness or new candidates/individuals
#mutation does not need to be implemented, but eventually all permutation of candidates with old genes from crossover will be implemented
#mutation is needed to create new candidates with NEW genes
#mutation brings more candidates in to population if population has been homogenized
#it is very important to implement randomness for convergence
def mutate(individual):
    #mutations may be small or large - play with intervals
    nextX0 = individual["x0"] + random.uniform(-0.05, 0.05)
    nextY0 = individual["y0"] + random.uniform(-0.05, 0.05)
    nextX1 = individual["x1"] + random.uniform(-0.05, 0.05)
    nextY1 = individual["y1"] + random.uniform(-0.05, 0.05)
    lowerBoundary, upperBoundary = (MIN_X, MAX_X)
    nextX0 = min(max(nextX0, lowerBoundary), upperBoundary)
    nextY0 = min(max(nextY0, lowerBoundary), upperBoundary)
    nextX1 = min(max(nextX1, lowerBoundary), upperBoundary)
    nextY1 = min(max(nextY1, lowerBoundary), upperBoundary)
    return {"x0": nextX0, "y0": nextY0, "x1": nextX1, "y1": nextY1}


#make next generation of genes after mutation and crossover is complete
#consider growing population with each successive generation, like actual evolution
#older genes/candidates/individuals could "live" for a few generations before they "die" and are removed from the population
#this would allow nested mutations and interesting crossovers
def makeNextGeneration(previousPopulation):
    nextGeneration = []
    sortedByFitnessPopulation = sortPopulationByFitness(previousPopulation)
    populationSize = len(previousPopulation)
    fitnessSum = sum(applyFunction(individual) for individual in population)
    for i in range(populationSize):
        firstChoice = choiceByRoulette(sortedByFitnessPopulation, fitnessSum)
        secondChoice = choiceByRoulette(sortedByFitnessPopulation, fitnessSum)
        individual = crossover(firstChoice, secondChoice)
        individual = mutate(individual)
        nextGeneration.append(individual)
    return nextGeneration


#MAIN
population = generatePopulation(size=POPULATION_SIZE, xBoundaries=(MIN_X, MAX_X), yBoundaries=(MIN_Y, MAX_Y))
x0ToGraph = []
y0ToGraph = []
x1ToGraph = []
y1ToGraph = []
fitX0ToGraph = []
fitY0ToGraph = []
fitX1ToGraph = []
fitY1ToGraph = []
index = 1

while True:
    print("generation {i}")
    for individual in population:
        print("individual:")
        print(individual)
        x0ToGraph.append(individual["x0"])
        y0ToGraph.append(individual["y0"])
        x1ToGraph.append(individual["x1"])
        y1ToGraph.append(individual["y1"])
        if index > (len(population) - 1):
            fitX0ToGraph.append(individual["x0"])
            fitY0ToGraph.append(individual["y0"])
            fitX0ToGraph.append(individual["x1"])
            fitY0ToGraph.append(individual["y1"])
    if index == GENERATIONS:
        break
    index += 1
    population = makeNextGeneration(population)

#survival of the fittest - closest solution
bestIndividual = sortPopulationByFitness(population)[-1]
print("\n\nfinal result " + str(bestIndividual) + " " + str(applyFunction(bestIndividual)))

if SHOULD_GRAPH:
    plt.plot(x0ToGraph, y0ToGraph, label='Evolution Line (First Pair)', color='Magenta')
    plt.legend(loc='upper left')
    plt.show()
    plt.clf()

    plt.plot(x1ToGraph, y1ToGraph, label='Evolution Line (Second Pair)', color='Magenta')
    plt.legend(loc='upper left')
    plt.show()
    plt.clf()

    colors = np.random.rand(4)
    plt.scatter(fitX0ToGraph, fitY0ToGraph, s=30, c=colors, alpha=0.5)
    plt.legend(loc='upper left')
    plt.show()

    colors = np.random.rand(4)
    plt.scatter(fitX1ToGraph, fitY1ToGraph, s=30, c=colors, alpha=0.5)
    plt.legend(loc='upper left')
    plt.show()


