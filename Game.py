import pygame
import Pygame_Plus as pg_plus

knight = pg_plus.Kvadrat(18, 18, 64, 64, 0, 0, pg_plus.color.black)

pos = [(18, 18)]

pos_to_go = []


def WhereToGo(x, y, bl):
    return [(x + bl, y - bl * 2), (x + bl * 2, y - bl), (x + bl * 2, y + bl), (x + bl, y - bl * 2), (x - bl, y + bl * 2), (x - bl * 2, y - bl), (x - bl * 2, y - bl), (x - bl, y - bl * 2)]


def DrAw():
    pass


pygame.init()