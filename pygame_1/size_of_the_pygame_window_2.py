import pygame 
pygame.init()


screen = pygame.display.set_mode((500 , 1200))

# get the size of the screen
x , y = screen.get_size()

# quit pygame 
running = True 
while(running==True): 
    for event in pygame.event.get() :   
        if event.type ==pygame.QUIT: 
            running ==False

# viewt he size ( width c height )
print(x , y)