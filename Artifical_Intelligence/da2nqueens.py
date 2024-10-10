import random

# Define the fitness function
def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    
    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

# Define the crossover function
def crossover(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

# Define the mutation function
def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

# Define the genetic algorithm
def genetic_queen(population, fitness):
    mutation_probability = 0.1
    new_population = []
    probabilities = [fitness(n) for n in population]
    for i in range(len(population)):
        x = random_choice(population, probabilities) # Parent selection
        y = random_choice(population, probabilities) # Parent selection
        child = crossover(x, y) # Crossover
        if random.random() < mutation_probability:
            child = mutate(child) # Mutation
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

# Define the random choice function
def random_choice(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

# Define the hill climbing algorithm with steepest-ascent variant
def steepest_ascent_hill_climbing(chromosome):
    current = chromosome
    while True:
        neighbors = [mutate(current) for _ in range(100)] # Generate neighbors
        next_chromosome = max(neighbors, key=fitness) # Choose the best neighbor
        if fitness(current) >= fitness(next_chromosome): # If no better neighbor, return current
            return current
        current = next_chromosome # Move to the next chromosome

# Define the hill climbing algorithm with first-choice variant
def first_choice_hill_climbing(chromosome):
    current = chromosome
    while True:
        neighbors = [mutate(current) for _ in range(100)] # Generate neighbors
        next_chromosome = None
        for neighbor in neighbors:
            if fitness(neighbor) > fitness(current): # Choose the first better neighbor
                next_chromosome = neighbor
                break
        if next_chromosome is None: # If no better neighbor, return current
            return current
        current = next_chromosome # Move to the next chromosome

# Now we need to generate the initial population
num_queens = 8
maxFitness = (num_queens*(num_queens-1))/2  # 8*7/2 = 28
population = [[random.randint(1, num_queens) for _ in range(num_queens)] for _ in range(10)]

# Display the 8-queens instances being used
print("8-queens instances being used:")
for instance in population:
    print(instance)

# Solve the instances using the genetic algorithm
print("\nSolutions using the genetic algorithm:")
for generation in range(20):
    population = genetic_queen(population, fitness)
    best_fit = max(list(map(fitness, population)))
    if best_fit == maxFitness: break

final_solution = []
for chrom in population:
    if fitness(chrom) == maxFitness:
        if chrom not in final_solution:
            final_solution.append(chrom)
print("Solutions: ")
for sol in final_solution:
    print(sol)

# Solve the instances using the steepest-ascent hill climbing algorithm
print("\nSolutions using the steepest-ascent hill climbing algorithm:")
for instance in population:
    solution = steepest_ascent_hill_climbing(instance)
    print("Solution: ", solution)

# Solve the instances using the first-choice hill climbing algorithm
print("\nSolutions using the first-choice hill climbing algorithm:")
for instance in population:
    solution = first_choice_hill_climbing(instance)
    print("Solution: ", solution)
