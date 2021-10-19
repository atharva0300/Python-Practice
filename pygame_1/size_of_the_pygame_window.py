import pygame 
pygame.init()

# form the screen
screen = pygame.display.set_mode()

# get the defualt size of the screen
x , y = screen.get_size()

# quit pygame
pygame.display.quit()

# view the size of the screen ( width x height)
print(x , y)

