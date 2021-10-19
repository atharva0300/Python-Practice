import pygame
pygame.init() 


screen = pygame.display.set_mode((250 , 250) , pygame.RESIZABLE) 

pygame.display.set_caption("person")

# RGB Color 
color= (255, 0,0)

# changing the screen color 
screen.fill(color )
# flip() is to update the screen 
pygame.display.flip()

# instead of flip() , you acan also use update() 
# like - pygame.display.update()

# loading an image  we want to use 
person = pygame.image.load("penguin.jpg")

# displaying the icon 
pygame.display.set_icon(person)

running = True
while(running ):
    for event in pygame.event.get() :
        if event.type==pygame.QUIT: 
            running = False 
            
