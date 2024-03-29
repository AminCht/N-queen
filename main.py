import random

import pygame as game

dimension = None
width = None
height = None
sq_size = None


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
    children = []
    for chrom in chromosomes:
        fitness = fitness_func(chrom)
        fitness_of_chromosomes.append(fitness)
        chrom_dict.append((fitness, chrom))
    mutate_prob = 5
    for j in range(len(chromosomes)):
        first_chromosome = selection(chrom_dict, int(sum(fitness_of_chromosomes)))
        second_chromosome = selection(chrom_dict, int(sum(fitness_of_chromosomes)))
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
    for k in range(len(first_chrom)):
        t = random.randint(0, 10)
        x = first_chrom[k]
        y = second_chrom[k]
        if t <= 5:
            first_chrom[k] = y
            second_chrom[k] = x
    return [first_chrom] + [second_chrom]


def best_chromosome(chromosome):
    print(chromosome)


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
        width = height = 512
        sq_size = height / dimension
        game.init()
        game.display.set_caption('N-queen')
        screen = game.display.set_mode((512, 512))
        screen.fill(game.Color('white'))
        while (finish == False):
            bestfitness = (number_of_q * (number_of_q - 1)) / 2
            best_chrom_found = False
            count = 0
            chromosomes = []
            while count < 4 and not best_chrom_found:

                for i in range(4):
                    chromosomes += [[random.randint(0, number_of_q - 1) for x in range(number_of_q)]]
                    # fitness = fitness_func(chromosomes[i])
                    # if fitness_func(chromosomes[i]) == bestfitness:
                    #     #best_chromosome(chromosomes[i])
                    #     best_chrom_found = True
                    count += 1
            if not best_chrom_found:
                chromosomes = genetic_algorithm(chromosomes)

                for h in chromosomes:
                    if bestfitness == fitness_func(h):
                        print('answer is: ')
                        print(h)
                        running = True
                        draw_board(screen)
                        draw_pieces(screen, h)
                        game.display.flip()
                        while running:
                            for e in game.event.get():
                                if e.type == game.QUIT:
                                    running = False
                                    game.quit()
                        finish = True
                        break
