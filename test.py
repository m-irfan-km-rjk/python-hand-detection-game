import pygame


win = pygame.display.set_mode((500,500))
s = pygame.image.load("img/blast.png")

clock = pygame.time.Clock()


while True:
    clock.tick(60)

    win.blit(s,(0,0),(0,96,100,95))

    for event in pygame.event.get():
        if event == pygame.QUIT:
            quit()

    pygame.display.update()