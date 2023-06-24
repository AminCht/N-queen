import random

import pygame as game

dimension = None
width = 512
height = 512
sq_size = None


def fitness_func(chromosome):
    vertical_collision = 0
    for m in chromosome:
        vertical_collision += chromosome.count(m) - 1
    vertical_collision /= 2
    matrix = []
    j = 0
    for i in chromosome:
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
    for k in chromosome:
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
    return int(best_fitness - (vertical_collision + diagonal_collision))


def genetic_algorithm(chromosomes):
    fitness_of_chromosomes = []
    chromosome_dict = []
    children = []
    for chromosome in chromosomes:
        fitness = fitness_func(chromosome)
        fitness_of_chromosomes.append(fitness)
        chromosome_dict.append((fitness, chromosome))
    mutate_prob = 5
    for j in range(len(chromosomes)):
        first_chromosome = selection(chromosome_dict, int(sum(fitness_of_chromosomes)))
        second_chromosome = selection(chromosome_dict, int(sum(fitness_of_chromosomes)))
        children += (crossover(first_chromosome, second_chromosome))
        if random.randint(0, 10) > mutate_prob:
            children.append(mutation(children[len(children) - 1]))

    return children


def mutation(child):
    place_of_gen = random.randint(0, len(child) - 1)
    random_gen = random.randint(0, len(child) - 1)
    child[place_of_gen] = random_gen
    return child


# using roulette wheel selection algorithm
def selection(chromosome_dict, sum_fitness):
    random_select = random.randint(1, sum_fitness)
    wheel = 0
    while wheel < random_select:
        for j, k in chromosome_dict:
            if wheel + j >= random_select:
                return k
            wheel += j


#
def crossover(first_chromosome, second_chromosome):
    for k in range(len(first_chromosome)):
        t = random.randint(0, 10)
        x = first_chromosome[k]
        y = second_chromosome[k]
        if t <= 5:
            first_chromosome[k] = y
            second_chromosome[k] = x
    return [first_chromosome] + [second_chromosome]


def best_chromosome(chromosome):
    print('answer is: ')
    print(chromosome)

    game.init()
    game.display.set_caption('N-queen')
    screen = game.display.set_mode((512, 512))
    screen.fill(game.Color('white'))
    running = True
    draw_board(screen)
    draw_pieces(screen, chromosome)
    game.display.flip()
    while running:
        for e in game.event.get():
            if e.type == game.QUIT:
                running = False
                game.quit()


def draw_board(screen):
    colors = [game.Color("white"), game.Color("grey")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            game.draw.rect(screen, color, game.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


def draw_pieces(screen, board):
    image = game.transform.scale(game.image.load("images/i.png"), (sq_size, sq_size))
    for c in range(dimension):
        screen.blit(image, game.Rect(c * sq_size, board[c] * sq_size, sq_size, sq_size))


if __name__ == '__main__':
    while True:
        finish = False
        number_of_q = int(input("Please insert number of queens:"))
        dimension = number_of_q
        sq_size = height / dimension
        best_fitness = (number_of_q * (number_of_q - 1)) / 2
        best_chromosome_found = False
        while not finish:
            count = 0
            chromosomes = []
            while count < 4 and not best_chromosome_found:

                for i in range(4):
                    chromosomes += [[random.randint(0, number_of_q - 1) for x in range(number_of_q)]]
                    fitness = fitness_func(chromosomes[i])
                    if fitness_func(chromosomes[i]) == best_fitness:
                        best_chromosome(chromosomes[i])
                        best_chromosome_found = True
                        finish = True
                        break
                    count += 1
            if not best_chromosome_found:
                chromosomes = genetic_algorithm(chromosomes)

                for h in chromosomes:
                    if best_fitness == fitness_func(h):
                        best_chromosome(h)
                        finish = True
                        break
