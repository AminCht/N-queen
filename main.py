import pygame as game

dimension = 8
width = height = 512
sq_size = height / dimension


class GameState:
    def __init__(self):
        self.board = [
            ["a", "b"]
        ]


def draw_board(screen):
    colors = [game.Color("white"), game.Color("grey")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            game.draw.rect(screen, color, game.Rect(c * sq_size, r * sq_size, sq_size, sq_size))


if __name__ == '__main__':
    game.init()
    screen = game.display.set_mode((512, 512))
    screen.fill(game.Color('white'))
    running = True
    while running:
        for e in game.event.get():
            if e.type == game.QUIT:
                running = False
        draw_board(screen)
        game.display.flip()
