#sum(xi ^ 2)
#-5.12 <= xi <= 5.12
# xi = 0
# i = 1 , 2 , ... , n

import random
import matplotlib.pyplot as plt

def fitness_function(chromosome):
    return sum(x**2 for x in chromosome)

# Creating the initial population
def generate_population(pop_size, lower_bound, upper_bound, num_variables):
    population = []
    for i in range(pop_size):
        chromosome = []
        for j in range(num_variables):
            chromosome.append(random.uniform(lower_bound, upper_bound))
        population.append(chromosome)
    return population

# select parents
def selection(population, fitness):
    selected = []
    for p in range(len(population)):
        i, j = random.sample(range(len(population)), 2)
        selected.append(population[i] if fitness[i] < fitness[j] else population[j])
    return selected

# produce new children from the parent
def crossover(parent1, parent2, crossover_rate=0.8):
    if random.random() < crossover_rate:
        point = random.randint(0, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2

#Applying random mutations to a chromosome
def mutation(chromosome, mutation_rate=0.2, lower_bound=-5.12, upper_bound=5.12):
    mutated_chromosome = []
    for gene in chromosome:
        if random.random() < mutation_rate:
            new_gene = random.uniform(-1, 1)
            bounded_gene = max(lower_bound, min(upper_bound, new_gene))
            mutated_chromosome.append(bounded_gene)
        else:
            mutated_chromosome.append(gene)
    return mutated_chromosome

#genetic_algorithm
def genetic_algorithm(pop_size, lower_bound, upper_bound, generations, num_variables):
    population = generate_population(pop_size, lower_bound, upper_bound, num_variables)
    # Show the best value in each generation
    best_fitness_values = []
    for g in range(generations):
        fitness = [fitness_function(chrom) for chrom in population]
        best_fitness = min(fitness)
        best_fitness_values.append(best_fitness)
        best_chromosome = population[fitness.index(best_fitness)]
        print(f"in generation {g+1} --> the best fitness in each section : {best_fitness:.4f},the best chromosome in each section : {best_chromosome}")
        # find the best fitness and chromosome
        selected_population = selection(population, fitness)
        next_population = []
        for i in range(0, len(selected_population), 2):
            parent1, parent2 = selected_population[i], selected_population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            next_population.append(mutation(child1, lower_bound=lower_bound, upper_bound=upper_bound))
            next_population.append(mutation(child2, lower_bound=lower_bound, upper_bound=upper_bound))
        population = next_population

    final_fitness = [fitness_function(chrom) for chrom in population]
    best_fitness = min(final_fitness)
    best_chromosome = population[final_fitness.index(best_fitness)]
    print("_ final answer _")
    print(f"Best fitness: {best_fitness:.4f}")
    print(f"Best chromosome: {best_chromosome}")

    # Plotting the results
    plt.plot(range(1, generations + 1), best_fitness_values, marker='o')
    plt.title("Best Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid()
    plt.savefig('D:/university/term-7/AI_project/genetic/code_genetic/genetic/output_plot.png')

# Parameters
POP_SIZE = 50
LOWER_BOUND = -5.12
UPPER_BOUND = 5.12
GENERATIONS = 100
NUM_VARIABLES = 5

genetic_algorithm(POP_SIZE, LOWER_BOUND, UPPER_BOUND, GENERATIONS, NUM_VARIABLES)
