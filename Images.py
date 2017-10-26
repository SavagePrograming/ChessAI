__author__ = 'william'
import pygame
Board = pygame.image.load('pictures/chess2.jpg')
class White():
    king = pygame.image.load('pictures/king.png')
    queen = pygame.image.load('pictures/queen.png')
    bishop = pygame.image.load('pictures/bishop.png')
    rook = pygame.image.load('pictures/rook.png')
    knight = pygame.image.load('pictures/knight.png')
    pawn = pygame.image.load('pictures/pawn.png')
class Black():
    king = pygame.image.load('pictures/bking.png')
    queen = pygame.image.load('pictures/bqueen.png')
    bishop = pygame.image.load('pictures/bbishop.png')
    rook = pygame.image.load('pictures/brook.png')
    knight = pygame.image.load('pictures/bknight.png')
    pawn = pygame.image.load('pictures/bpawn.png')