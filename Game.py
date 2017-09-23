import pygame
from snake import Snake
from food import Food

pygame.init()
screen = pygame.display.set_mode((400, 300))

myfont = pygame.font.SysFont('Comic Sans MS', 20)
textsurface = myfont.render('0', False, (255, 255, 255))

done = False
color = (0, 128, 255)

clock = pygame.time.Clock()

s = Snake(map_dimensions=(400,300))
f = Food()
food_eaten = False
f.generate(s.position)

GAME_OVER = False
UP_DIR = False
DOWN_DIR = True
RIGHT_DIR = False
LEFT_DIR = False

while not done and not GAME_OVER:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and not DOWN_DIR:
            UP_DIR = True
            DOWN_DIR = False
            RIGHT_DIR = False
            LEFT_DIR = False
        if pressed[pygame.K_DOWN] and not UP_DIR:
            UP_DIR = False
            DOWN_DIR = True
            RIGHT_DIR = False
            LEFT_DIR = False
        if pressed[pygame.K_LEFT] and not RIGHT_DIR:
            UP_DIR = False
            DOWN_DIR = False
            RIGHT_DIR = False
            LEFT_DIR = True
        if pressed[pygame.K_RIGHT] and not LEFT_DIR:
            UP_DIR = False
            DOWN_DIR = False
            RIGHT_DIR = True
            LEFT_DIR = False

        if UP_DIR:
            s.update_tail()
            s.update_head(y=-10)
        if DOWN_DIR:
            s.update_tail()
            s.update_head(y=10)
        if LEFT_DIR:
            s.update_tail()
            s.update_head(x=-10)
        if RIGHT_DIR:
            s.update_tail()
            s.update_head(x=10)

        screen.fill((0,0,0))
        textsurface = myfont.render(str(len(s.position)-2) , False, (255, 255, 255))
        screen.blit(textsurface,(0,0))

        if s.position[0] == f.position():
            food_eaten = True

        for i in range(1,len(s.position)):
            if s.position[0] == s.position[i]:
                GAME_OVER = True
                print 'Game Over !!'
                break

        if food_eaten:
            s.eat(f.position()[0], f.position()[1])
            f.generate(s.position)
            food_eaten = False

        f.draw(screen)
        s.draw(screen, color)

        #print 'Snake: ', s.position[0] ## Debug
        #print 'Food: ', f.position() ## Debug

        pygame.display.flip()
        clock.tick(15)
