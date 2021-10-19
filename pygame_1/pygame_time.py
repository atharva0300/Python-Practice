import pygame
pygame.init() 
    

screen = pygame.display.set_mode((1000 , 1000) , pygame.RESIZABLE) 

pygame.display.set_caption("person")

# pygame-time : fucntions fiscussed 
# pygame.time.wait
# pygame.time.get_ticks 
# pygame.time.delay
# pyagme.yime.Clock


# pygame.time.wait
# the function is used to pause the running of the progeam for a few seconds 
pygame.time.wait(5000)

person = pygame.image.load("tom.jpg")
screen.blit(person , (0 , 0))
pygame.display.update()

# pygame.time.get_ticks()  - 
# this function gives a time which has been running in milliseconds 
i = 0
while(i<5): 
    ticks = pygame.time.get_ticks() 
    print(ticks)
    
    i = i+1 
    pygame.time.wait(2000)
    
# pygame.time.delay - 
# This function works the same as pygame.time.wait function 
# the difference is that this function will use the procesor ( rather than sleeping ) in order to make the delay more accurate 
pygame.time.delay(5000)
screen.blit(person , (500 , 0 ))
pygame.display.update()

# pygame.time.clock - 
# the function is used to create a clokc object wich can be used 
# to leep track of time.

# tick() - This methos sohuld be called once per frame 
# it will compute how many milliseconds have passed since the previous call. If you pas the optional framerate , argument the function will delay to leep the game running slower than the given ticks per second.
 # for example - if we pass 10 as the argument, the program will never run at more than 10 frmes per second 

# get_time() - it is used to obtain a number of millisecond used between two tick() 

# get_fps() - it gives the information regarding the clock frame rate. it returns the output in floating-point value 

clock = pygame.time.Clock()
i = 0
while(i<5) : 
    # setting fps of the program to max 1 per second 
    clock.tick(1)
    
    # printing the time used in the previous tick
    print(clock.get_time())
    
    # printing the compute the clock framerate 
    print(clock.get_fps())
    i = i+1

running = True 
while(running): 
    for event in pygame.event.get() : 
        if event.type==pygame.QUIT: 
            running = False 
    
            