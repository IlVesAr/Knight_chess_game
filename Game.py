import pygame
import Pygame_Plus as pg_plus

knight = pg_plus.Kvadrat(318, 318, 64, 64, 0, 0, pg_plus.color.black)

pos = [(18, 18)]

pos_to_go = []


def WhereToGo(x, y, bl):
    return [(x + bl, y - bl * 2), (x + bl * 2, y - bl), (x + bl * 2, y + bl), (x + bl, y + bl * 2), (x - bl, y + bl * 2), (x - bl * 2, y + bl), (x - bl * 2, y - bl), (x - bl, y - bl * 2)]


def DrAw(win):
    win.blit(board, (0, 0))
    for i in pos_to_go:
        win.blit(where, (i[0] + 10, i[1] + 10))
    win.blit(kon, (knight.x, knight.y))
    pygame.display.update()


width, height = 800, 800
pygame.init()
win = pygame.display.set_mode((width, height))

board = pygame.image.load('Resouces/chessboard.jpg')
kon = pygame.image.load('Resouces/knight.png')
where = pygame.image.load('Resouces/Circle.png')


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos_to_go = WhereToGo(knight.x//100 * 100, knight.y//100 * 100, 100)
    DrAw(win)

pygame.quit()