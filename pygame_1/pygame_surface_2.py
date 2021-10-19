import pygame
pygame.init() 
    

screen = pygame.display.set_mode((2000 , 1000) , pygame.RESIZABLE) 

pygame.display.set_caption("person")

color = (230, 120, 134)

screen.fill(color)

pygame.display.update()
# loadig the image on the surface 
person = pygame.image.load("tom.jpg")

# putting out image surface on th display 
# surface 
screen.blit(person,(25 ,25))
pygame.display.update()

screen.blit(person ,(25, 500))
pygame.display.update()

# pygame.surface.convert() - it makes a copy of the surface with pixel format changed. the new pixel format can be determined from an 
# existing surface or depth , flags , and masks arguments can be used.

pygame.Surface.convert(screen)
pygame.display.update()

# pygame.Surface.convert_alpha() - it creates a new copy of the surface ith rhe desired pixel format.
# the new surface will be in a format suited for quick blitting to given format wirh per-pixel alpha.
# if no surface is given, the new surface will be optimized for blitting to the 
# current display 

pygame.Surface.convert_alpha(screen)
pygame.display.update()


# pygame.Surface.copy() - it creates a new copy of the surface, 
# the diplicate surface will have the same pixel formats , color ,palettes , transperency settings , and class as the original 

copied_surface = pygame.Surface.copy(screen)
pygame.display.update()



# pygame.Surface.set_colorkey - Set the current color key for the surface. 
# when blitting this surface onto a destination , any pixels 
# that have the same color as the colorkey will be transparent 

pygame.Surface.set_colorkey(person , [255,255,255])
screen.blit(person , (1000 , 500))
pygame.display.update()

# gets the color key value which was set for the 
# image
print(pygame.Surface.get_colorkey(person))

# pygame.Surface.set_alpha - The alpha value set for the full surface image 
# pass 0 for invisible and 255 for fully opaque 
# the higher the value , the more opaque it will be ( ie- the more clearer)
# the lower the value , the more trasparet the image will look ( ie - trasparent  ,not so clear)
pygame.Surface.set_alpha(person , 30)
screen.blit(person , (1000 , 25))
pygame.display.update()

running = True 
while(running): 
    for event in pygame.event.get() : 
        if event.type==pygame.QUIT: 
            running = False 
    
            