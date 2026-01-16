import pygame
import random
import math


# initialize the pygame 
pygame.init()


# create the screen and gave the height and width and used setmode 
screen= pygame.display.set_mode((800,600)) 


# background add
bg= pygame.image.load('bg2.png.png')


# title and icon
pygame.display.set_caption("conor mcgregor")
icon= pygame.image.load('image.png')
pygame.display.set_icon(icon)


# creating player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerXchange=0
playerYchange=0


# enemy 
enemyImg=pygame.image.load('monster.png')
enemyX=random.randint(0,735)
enemyY=random.randint(30,140)
enemyXchange=0.3
enemyYchange=0


# ready- u cant see the bullet
# fire-the bullet is firing man
# bullet 
bulletImg=pygame.image.load('beer.png')
bulletX=0
bulletY=480
bulletXchange=0
bulletYchange=2.5
bulletState="ready"

score=0


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fireBullet(x,y):
    global bulletState
    bulletState= "fire"
    screen.blit(bulletImg,(x+16,y+10))
# blit use to display the image x and y are cordinates

# collison 
def collision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((math.pow(enemyX - bulletX,2))+ (math.pow(enemyY - bulletY,2)))
    if distance<27:
        return True
    else:
        return False


# gameloop
running= True
while running:

    screen.fill((240,128,128))
# now we willl give bg color to it 

    # backgroundimage
    screen.blit(bg,(0,0))
   


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
                playerXchange=-1
            if event.key==pygame.K_RIGHT:
                playerXchange=1

            if event.key==pygame.K_UP:
                playerYchange=-1
            if event.key == pygame.K_DOWN:
                playerYchange = 1
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletX= playerX
                    fireBullet(bulletX,bulletY)
            

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
        enemyY+=30
    elif enemyX>=736:
        enemyXchange=-0.3
        enemyY+=30

    
    # bullet movement 
    if bulletY <=0:
        bulletY= 480 
        bulletState= "ready"
    if bulletState == "fire":
        fireBullet(bulletX,bulletY)
        bulletY-=bulletYchange 

    
    # obstacle
    obstacle= collision(enemyX,enemyY,bulletX,bulletY)
    if obstacle:
        bulletY=480
        bulletState="ready"
        score+=1
        print(score)
        enemyX=random.randint(0,735)
        enemyY=random.randint(30,140)


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()




# we changed the value of x and y means we gave it to the player  when we close the function









# we can add y direction which can control the movement for up and down 