import pygame
import random

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
playerXchange=0
playerYchange=0


# enemy 
enemyImg=pygame.image.load('khabib.png')
enemyX=random.randint(0,800)
enemyY=random.randint(30,140)
enemyXchange=0.3
enemyYchange=0
# playerYchange=0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

# blit use to display the image x and y are cordinates


# gameloop
running= True
while running:

    screen.fill((240,128,128))
# now we willl give bg color to it 
   


#this is given to control the movemeent that it will go left or right or  up and down
    # playerX+=0.1
    # playerX-=0.1
    # playerY+=0.1
    # playerY-=0.1
   



    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
# here in loop we gave it true then in running we gave like system to quit the screen so it no lags when we click on quit button. and with this windows stays forever 


# if keystroke is pressed check its left or right

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXchange=-0.3
            if event.key==pygame.K_RIGHT:
                playerXchange=0.3

            if event.key==pygame.K_UP:
                playerYchange=-0.3
            if event.key == pygame.K_DOWN:
                playerYchange = 0.3

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerXchange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerYchange=0

    # 5=5+-0.1 -> 5 - 0.1
    playerX+=playerXchange
    playerY+=playerYchange


    # boundry for x //  here it should not exceed 736 as here img is 64x64 so it will overcross the boundry so to avoid it we minus it from 800 and what left we gave it to that
    if playerX <=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:  # 600 - 64 (image height)
        playerY = 536

    

    enemyX+=enemyXchange
    # enemyY+=enemyYchange

    if enemyX <=0:
        enemyXchange=0.3
        enemyY+=10
    elif enemyX>=736:
        enemyXchange=-0.3
        enemyY+=10

    


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()




# we changed the value of x and y means we gave it to the player  when we close the function









# we can add y direction which can control the movement for up and down 