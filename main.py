import pygame, sys
from settings import WIDTH, HEIGHT, NAV_THICKNESS
from world import World


#stup pygame environnement
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_THICKNESS))
pygame.display.set_caption("Space Invader")
run = True


#setup des valeurs
score_value = 0
x = (width*0.95)        
y = (height*0.5)
vel = 1

#isep image
character = pygame.image.load('isep.png')
def add_character_at_location(x,y):
    screen.blit(character, (x,y))

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
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

    #keys 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (x,y,width,height))
    pygame.display.update()



pygame.quit()