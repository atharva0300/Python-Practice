# import the pygame package 
import pygame 
# iitialize the pygame with pygame.init()
pygame.init()


# set the size of the display screen
pygame.display.set_mode((200 , 300))

running = True 
# while running==True , the window will keep refreshing and the program 
# will keep running , the window won't close 
# but , if we press the quit button  
# then the program closes , the window closes as well
while running : 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running = False
