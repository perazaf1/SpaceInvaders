import pygame

pygame.init()
width = 30
height = 20

screen = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
run = True

x = 50
y = 50
vel = 0.3

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    #screen.fill((30,30,30))
    #pygame.display.flip()

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