import math
import pygame
import time
import random
import sys


#Setup de pygame
pygame.init()
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
running = True

# caption and icon
pygame.display.set_caption("Space Invaders")
screen_icon = pygame.image.load('')


#setup des valeurs
score_value = 0
scoreX = 5
scoreY = 5

font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

#function to show the score
def show_score(x, y):
    score = font.render("Points: " + str(score_value),
                        True, (255,255,255))
    screen.blit(score, (x , y ))
 
#function when game is over
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))

#setup to make invaders game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30,30,30))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


if ket