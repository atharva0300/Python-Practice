import pygame
pygame.init() 
    

screen = pygame.display.set_mode((250 , 250) , pygame.RESIZABLE) 

pygame.display.set_caption("person")

person = pygame.image.load("penguin.jpg")

running = True 
while(running): 
    for event in pygame.event.get() : 
        if event.type==pygame.QUIT: 
            running = False 
    
    pygame.display.set_icon(person)
    pygame.display.update()
    
    if(person=="penguin.jpg") : 
        person = pygame.image.load("tom.jpg")
    
    else : 
        person = pygame.image.load("penguin.jpg")
    
            