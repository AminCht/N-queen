import random


def fitness_func(chrom):
    vertical_collision = 0
    for m in chrom:
        vertical_collision += chrom.count(m) - 1
    vertical_collision /= 2
    matrix = []
    j = 0
    for i in chrom:
        matrix.append([])
        for k in range(number_of_q):
            if k == i:
                matrix[j].append('q')
            else:
                matrix[j].append('0')
        j += 1
    diagonal_collision = 0
    j = 0
    i = 0
    for k in chrom:
        j = k
        ii = i
        jj = j
        while (ii + 1) in range(number_of_q) and (jj + 1) in range(number_of_q):
            if matrix[i][j] == matrix[ii + 1][jj + 1]:
                diagonal_collision += 1
                ii += 1
                jj += 1
                break
            ii += 1
            jj += 1
        ii = i
        jj = j
        while (ii + 1) in range(number_of_q) and (jj - 1) in range(number_of_q):
            if matrix[i][j] == matrix[ii + 1][jj - 1]:
                diagonal_collision += 1
                ii += 1
                jj -= 1
                break
            ii += 1
            jj -= 1
        i += 1
    return int(bestfitness - (vertical_collision + diagonal_collision))


def genetic_algorithm(chromosomes):
    fitness_of_chromosomes = []
    chrom_dict = []
    children_mutated = []
    for chrom in chromosomes:
        fitness = fitness_func(chrom)
        fitness_of_chromosomes.append(fitness)
        chrom_dict.append((fitness, chrom))
    mutate_prob = 0.5
    for j in range(len(chromosomes)):
        first_chromosome = selection(chrom_dict, int(sum(fitness_of_chromosomes)))
        second_chromosome = selection(chrom_dict, int(sum(fitness_of_chromosomes)))
        children = crossover(first_chromosome, second_chromosome)
        if random.uniform(0, 1) >= mutate_prob:
            children = mutation(children)

#        if bestfitness in [fitness_func(chrom) for chrom in children]:
    return children


def mutation(child):
    place_of_gen = random.randint(0, len(child) - 1)
    random_gen = random.randint(0, len(child) - 1)
    child[place_of_gen] = random_gen
    return child




# using roulette wheel selection algorithm
def selection(chrom_dict, sum_fitnesses):
    random_select = random.randint(1, sum_fitnesses)
    wheel = 0
    while wheel < random_select:
        for j, k in chrom_dict:
            if wheel + j >= random_select:
                return k
            wheel += j


#
def crossover(first_chrom, second_chrom):
    c = [0] * len(first_chrom)
    for j in range(len(first_chrom)):
        r = random.randint(0, 1)
        if r < 0.5:
            c[j] = first_chrom[j]
        else:
            c[j] = second_chrom[i]
    return c
    # for j in range(len(first_chrom)):
    #     t = random.randint(0, 1)
    #     x = first_chrom[j]
    #     y = second_chrom[j]
    #     if t < 0.5:
    #         first_chrom[j] = y
    #         second_chrom[j] = x
    # return [first_chrom] + [second_chrom]



def best_chromosome(chromosome):

    print(chromosome)


if __name__ == '__main__':
    while True:
        number_of_q = int(input("Please insert number of queens:"))
        bestfitness = (number_of_q * (number_of_q - 1)) / 2
        best_chrom_found = False
        count = 0
        chromosomes = []
        while count < 100:

            for i in range(4):
                chromosomes += [[random.randint(0, number_of_q - 1) for x in range(number_of_q)]]
                # fitness = fitness_func(chromosomes[i])
                if fitness_func(chromosomes[i]) == bestfitness:
                    best_chromosome(chromosomes[i])
                    best_chrom_found = True
            count += 1
        if not best_chrom_found:
            chromosomes = genetic_algorithm(chromosomes)
            print("best is:")
            print(chromosomes)

