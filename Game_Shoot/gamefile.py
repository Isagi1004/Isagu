import pygame
import sys
import math
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
background=pygame.image.load('back.png')
pygame.display.set_caption("Nah I'd Win")
icon=pygame.image.load('nah.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('go.png')
playerX=370
playerY=480
playerX_change=0

enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no=6


for i in range(no):
    enemyimg.append(pygame.image.load('suku.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

purpimg=pygame.image.load('purp.png')
purpX=0
purpY=480
purpX_change=0
purpY_change=10  # =50 for hack
purp_state="ready"

scorev=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render("Score:"+str(scorev),True,(0,0,0))
    screen.blit(score,(x,y))


def game_over():
    over_text=over_font.render("GAME OVER",True,(0,0,0))
    screen.blit(over_text,(200,250))



def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire(x,y):
    global purp_state
    purp_state="fire"
    screen.blit(purpimg,(x+16,y+10))
def iscollide(enemyX,enemyY,purpX,purpY):
    distance=math.sqrt((math.pow(enemyX-purpX,2))+(math.pow(enemyY-purpY,2)))
    if distance<27:
        return True
    else:
        return False
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-3
            if event.key == pygame.K_RIGHT:
                playerX_change=3
            if event.key == pygame.K_SPACE:
                if purp_state == "ready":
                    purpX=playerX
                    fire(playerX,purpY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    for i in range(no):
        if enemyY[i]>250:
            for j in range(no):
                enemyY[j]=2000
            game_over()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=1
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-1
            enemyY[i]+=enemyY_change[i]

        collision=iscollide(enemyX[i],enemyY[i],purpX,purpY)
        if collision:
            purpY=480
            purp_state="ready"
            scorev+=10
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(0,150)
        
        enemy(enemyX[i],enemyY[i],i)


    if purpY<=0:
        purpY=480
        purp_state="ready"
    if purp_state == "fire":
        fire(purpX,purpY)
        purpY-=purpY_change
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
#pygame.display.quit()
pygame.quit()
#exit()
