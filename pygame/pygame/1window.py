import pygame

# initialize the pygame 
pygame.init()


# create the screen and gave the height and width and used setmode 
screen= pygame.display.set_mode((800,600)) 


# gameloop
running= True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
# here in loop we gave it true then in running we gave like system to quit the screen so it no lags when we click on quit button. and with this windows stays forever 