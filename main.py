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
    chrom_dict = {}
    for chrom in chromosomes:
        fitness = fitness_func(chrom)
        fitness_of_chromosomes.append(fitness)
        chrom_dict.update({fitness: chrom})

    for i in range(len(chromosomes)):
        first_chromosome = selection(chrom_dict, int(sum(fitness_of_chromosomes)))
        second_chromosome = selection(chrom_dict, int(sum(first_chromosome)))



# using roulette wheel selection algorithm
def selection(chrom_dict, sum_fitnesses):
    random_select = random.randint(0, sum_fitnesses)
    wheel = 0
    for j, k in chrom_dict:
        if wheel + j >= random_select:
            return k
        wheel += j


def best_chromosome(chromosome):
    print(chromosome)


if __name__ == '__main__':
    while True:
        number_of_q = int(input("Please insert number of queens:"))
        bestfitness = (number_of_q * (number_of_q - 1)) / 2
        best_chrom_found = False
        count = 0
        while count < 4:
            chromosomes = []
            for i in range(4):
                chromosomes += [[random.randint(0, number_of_q - 1) for x in range(number_of_q)]]
                # fitness = fitness_func(chromosomes[i])
                if fitness_func(chromosomes[i]) == bestfitness:
                    best_chromosome(chromosomes[i])
                    best_chrom_found = True
            count += 1
        if not best_chrom_found:
            chromosomes = genetic_algorithm(chromosomes)
