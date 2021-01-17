# importing stuff

from Scripts.Variables import *
from Scripts.Engine import *
import pygame

# initializing the variables to get assigned later in the initialize method
display = 0
board = 0



class Main:
    @staticmethod
    def onEveryFrame():

        x, y = pygame.mouse.get_pos()

        Board.draw_board(display)
        Board.draw_pieces(board, display)
        Board.draw_hovered_piece(display, hover_piece, x, y)
        pygame.display.update()

    @staticmethod
    def onRightClickDown(x, y):

        global hover_piece, took_from, avails

        row, column = helper.fromAxis(x, y)

        # assigning the available moves for the held piece
        avails = []
        if board[column][row] in chance :
            if board[column][row] == 1:
                avails = (Available.check_down(board, row, column, u))
            elif board[column][row] == 2:
                avails = (Available.check_up(board, row, column, d))
            elif board[column][row] == 3:
                avails = Available.check_king(board, row, column, u)
            elif board[column][row] == 4:
                avails = Available.check_king(board, row, column, d)



        hover_piece = board[column][row]
        took_from = [column, row]
        board[column][row] = 0

    @staticmethod
    def onRightClickUp(x, y):

        global hover_piece, avails, next, chance

        row, column = helper.fromAxis(x, y)
        if hover_piece != 0:

            if helper.fromIndex(column, row) in avails:
                board[column][row] = hover_piece
                res = helper.sub_list([column,row],[took_from[0],took_from[1]])
                if res[0] in [2,-2]:
                    to = helper.dev_list_by2(res)
                    board[took_from[0] + to[0]][took_from[1] + to [1]] = 0
                chance , next = next , chance
            else:
                board[took_from[0]][took_from[1]] = hover_piece
        hover_piece = 0
        avails = 0

        Board.check_promotion(board)


    @staticmethod
    def main():
        global board

        Main.initialize()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Main.onQuit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Main.onRightClickDown(event.pos[0], event.pos[1])

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        Main.onRightClickUp(event.pos[0], event.pos[1])

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        board = Board.newBoard()


            Main.onEveryFrame()

    @staticmethod
    def initialize():
        global display, board
        pygame.init()
        display = pygame.display.set_mode((dimension, dimension))
        pygame.display.set_caption("Checkers")
        board = Board.newBoard()

    @staticmethod
    def onQuit():
        quit()



Main.main()
