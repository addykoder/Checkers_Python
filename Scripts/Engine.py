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

                elif board[rows][block] == 3:

                    pygame.draw.circle(display, light_king, ((block * unit_size) + (unit_size // 2), (rows * unit_size) + (unit_size // 2)), (unit_size // 2) - 5)

                elif board[rows][block] == 4:

                    pygame.draw.circle(display, dark_king, ((block * unit_size) + (unit_size // 2), (rows * unit_size) + (unit_size // 2)), (unit_size // 2) - 5)

    @staticmethod
    def draw_hovered_piece(display, piece, x, y):
        if piece == 1:
            pygame.draw.circle(display, light_piece, (x, y), (unit_size//2)-5)
        elif piece == 2:
            pygame.draw.circle(display, dark_piece, (x, y), (unit_size // 2) - 5)
        elif piece == 3:
            pygame.draw.circle(display, light_king, (x, y), (unit_size // 2) - 5)
        elif piece == 4:
            pygame.draw.circle(display, dark_king, (x, y), (unit_size // 2) - 5)


    @staticmethod
    def newBoard():
        return [
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]

        ]

    @staticmethod
    def check_promotion(board):


        for i in range(8):
            if board[0][i] == 1:
                board[0][i] = 3
            if board[7][i] == 2:
                board[7][i] = 4




class Available:

    @staticmethod
    def check_down(board, row, column, opp):
        available = []

        if column != 0:
            if row != 0:
                if board[column-1][row-1] == 0:
                    available.append(helper.fromIndex(column-1, row-1))
            if row != 7:
                if board[column-1][row+1] == 0:
                    available.append(helper.fromIndex(column - 1, row + 1))


            if column != 1:
                if row != 0:
                    if row != 1:
                        if board[column - 2][row - 2] == 0 and board[column - 1][row - 1] in opp:
                            available.append(helper.fromIndex(column - 2, row - 2))
                if row != 7:
                    if row != 6:
                        if board[column - 2][row + 2] == 0 and board[column -1][row + 1] in opp:
                            available.append(helper.fromIndex(column - 2, row + 2))


        return available

    @staticmethod
    def check_up(board, row, column, opp):
        available = []

        if column != 7:
            if row != 0:
                if board[column + 1][row - 1] == 0:
                    available.append(helper.fromIndex(column + 1, row - 1))
            if row != 7:
                if board[column + 1][row + 1] == 0:
                    available.append(helper.fromIndex(column + 1, row + 1))

            if column != 6:
                if row != 0:
                    if row != 1:
                        if board[column + 2][row - 2] == 0 and board[column +1][row -1] in opp:
                            available.append(helper.fromIndex(column + 2, row - 2))
                if row != 7:
                    if row != 6:
                        if board[column + 2][row + 2] == 0 and board[column + 1][row + 1] in opp:
                            available.append(helper.fromIndex(column + 2, row + 2))

        return available

    @staticmethod
    def check_king(board, row, column, opp):

        available = Available.check_down(board, row, column, opp)
        for i in Available.check_up(board, row, column, opp):
            available.append(i)
        return available

class helper:
    # returns board indexes starting from 0
    @staticmethod
    def fromAxis(x, y):
        return (x // unit_size), (y // unit_size)

    # returns serial value from 1 to 64
    @staticmethod
    def fromIndex(x, y):
        return (x) * 8 + y + 1  # added one at the end because we have to start from 1

    # returns x and y index value
    @staticmethod
    def toIndex(serial):
        if serial % 8 != 0:
            return serial // 8, (serial % 8) - 1
        else:
            return (serial // 8) - 1, 7

    # returns the true x and y values
    @staticmethod
    def toAxis(x, y):
        return x * unit_size, y * unit_size

    @staticmethod
    def sub_list(list,list2):
        return [list[0] - list2[0] , list[1] - list2[1]]

    @staticmethod
    def dev_list_by2(list):
        return [list[0] // 2, list[1] // 2]

