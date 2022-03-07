import random

import ant_colony_optimization
import genetic_algorithm


GRID_SIZE = 100  # only used in random points generation

number_of_cities = input('Enter number of cities: ')
NUMBER_OF_CITIES = int(number_of_cities)
if NUMBER_OF_CITIES < 2:
    NUMBER_OF_CITIES = 2
points = []
# GENERATING RANDOM DATA
for j in range(NUMBER_OF_CITIES):
    x = random.uniform(0, GRID_SIZE)
    y = random.uniform(0, GRID_SIZE)
    points.append((x, y))

# STARTING GENETIC ALGORITHM
genetic_algorithm.execute(points, NUMBER_OF_CITIES)

# STARTING ANT COLONY OPTIMIZATION
ant_colony_optimization.execute(points, NUMBER_OF_CITIES)

