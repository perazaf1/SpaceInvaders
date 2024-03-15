import pygame
from shipisep import Ship
from opponents import Opponent
from settings import HEIGHT, WIDTH, ENEMY_SPEED, CHARACTER_SIZE, BULLET_SIZE, NAV_THICKNESS
from bullet import Bullet
from display import Display


class World:
    def __init__(self, screen):
        self.screen = screen
        self.player = pygame.sprite.GroupSingle()
        self.opponents = pygame.sprite.Group()
        self.display = Display(self.screen)
        self.game_over = False
        self.player_score = 0
        self.game_level = 1
        self._generate_world()

    def _generate_opponents(self):
        #generate opponents
        opponents_col = (WIDTH//CHARACTER_SIZE)// 2
        opponents_rows = 4
        for y in range (opponents_rows):
            for x in range(opponents_col):
                