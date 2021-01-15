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
        Board.draw_board(display)
        Board.draw_pieces(board, display)
        pygame.display.update()

    @staticmethod
    def onRightClickDown():
        pass

    @staticmethod
    def onRightClickUp():
        pass

    @staticmethod
    def main():
        Main.initialize()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Main.onQuit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Main.onRightClickDown()

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        Main.onRightClickUp()


            Main.onEveryFrame()

    @staticmethod
    def initialize():
        global display, board
        pygame.init()
        display = pygame.display.set_mode((dimension, dimension))
        pygame.display.set_caption("Checkers")
        board = Board.newBoard(8)

    @staticmethod
    def onQuit():
        quit()



Main.main()
