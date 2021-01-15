# importing stuff
import numpy
from Scripts.Variables import *
import pygame


class Board:

    @staticmethod
    def draw_board(display):
        block = unit_size
        cnt = 0
        for i in range(8):
            for j in range(8):
                axis = (i * block, j * block, block, block)
                if cnt % 2 == 0:
                    pygame.draw.rect(display, light_block, axis)
                else:
                    pygame.draw.rect(display, dark_block, axis)
                cnt += 1
            cnt -= 1

    @staticmethod
    def draw_pieces(board,display):
        for rows in range(units):
            for block in range(units):
                if board[rows][block] == 1:

                    pygame.draw.circle(display, light_piece, ((block * unit_size) + (unit_size//2), (rows * unit_size) + (unit_size//2)), (unit_size//2)-5)

                elif board[rows][block] == 2:

                    pygame.draw.circle(display, dark_piece, ((block * unit_size) + (unit_size//2), (rows * unit_size) + (unit_size//2)), (unit_size//2)-5)




    @staticmethod
    def newBoard(size):

        return numpy.array([
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]

        ])


