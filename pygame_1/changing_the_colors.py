import pygame 
pygame.init() 


screen = pygame.display.set_mode((250 , 250) , pygame.RESIZABLE) 

pygame.display.set_caption("person")

icon = pygame.image.load("penguin.jpg")
pygame.display.set_icon(icon)

color= "red"
running = True 
while(running) :
    for event in pygame.event.get( ): 
        if event.type==pygame.QUIT: 
            runniing = False 
    
    screen.fill(color)
    
    # update the window 
    pygame.display.update()
    
    # if the color id red , change the color to blue 
    if(color=="red" ) : 
        color = "blue"
    else : 
        color ="red"
    
            