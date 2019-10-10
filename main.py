import pygame

from game import Game
from maze import Maze

my_maze = Maze()

my_game = Game()

my_game.maze.display_maze(my_maze)

my_game.generate_maze()

my_game.maze.display_maze(my_maze)


running = True

"""Sometimes move function returns None, and gets out of the while running loop"""
while running != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            next_pos = my_game.set_position(event)
            running = my_game.move(next_pos)

    pygame.display.flip()
