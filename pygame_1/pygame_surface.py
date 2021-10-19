import pygame 
pygame.init() 

screen = pygame.display.set_mode((500 , 500) , pygame.RESIZABLE)
pygame.display.set_caption("person") 

color= (255, 255, 0)

# drawing a rectangle 

pygame.draw.rect(screen , color , pygame.Rect(30 , 30 , 60 , 60))

pygame.display.update()

running = True 
while(running): 
    for event in pygame.event.get() : 
        if event.type==pygame.QUIT: 
            running = False 