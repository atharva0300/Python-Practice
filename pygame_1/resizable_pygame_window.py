import pygame 
pygame.init()


screen = pygame.display.set_mode((400 , 400) , pygame.RESIZABLE)

# set title 
pygame.display.set_caption("person")

# run window 
running = True 
while (running): 
    for event in pygame.event.get() :
        if event.type==pygame.QUIT: 
            running = False 
           