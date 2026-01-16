import pygame

# initialize the pygame 
pygame.init()


# create the screen and gave the height and width and used setmode 
screen= pygame.display.set_mode((800,600)) 


# title and icon
pygame.display.set_caption("conor mcgregor")
icon= pygame.image.load('image.png')
pygame.display.set_icon(icon)


# creating player
playerImg=pygame.image.load('collaboration.png')
playerX=370
playerY=480

def player(x,y):
    screen.blit(playerImg,(x,y))

# blit use to display the image x and y are cordinates


# gameloop
running= True
while running:

    screen.fill((240,128,128))
# now we willl give bg color to it 
   


#this is given to control the movemeent that it will go left or right or  up and down
    # playerX+=0.1
    playerX-=0.1
    # playerY+=0.1
    # playerY-=0.1
   



    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
# here in loop we gave it true then in running we gave like system to quit the screen so it no lags when we click on quit button. and with this windows stays forever 



    player(playerX,playerY)
    pygame.display.update()




# we changed the value of x and y means we gave it to the player  when we close the function