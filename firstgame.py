import pygame
import random

pygame.init()

# The screen that will be created needs a width and a height.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

#creates the player,enemies and prize and gives it the images found in this folder.
player = pygame.image.load("goku.png")
enemy = pygame.image.load("enemy.jpg")
enemy2 = pygame.image.load("thanos.png")
enemy3 = pygame.image.load("player.png")
prize = pygame.image.load("prize.jpg") 

#the width and height of the images in order to do boundary detection
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()  

#Display, if you want to see the dimensions of the images 
print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player, enemies and prize as variables
playerXPosition = 100
playerYPosition = 50
prizeXPosition = 800
prizeYPostion = 500

#Makes the enemies start off screen and at a random y position
enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

#To check if below keys are pressed, make it False as in not pressed yet
keyUp= False
keyDown = False
keyLeft = False
keyRight = False

#create game loop
while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition)) 
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition)) 
    screen.blit(prize, (prizeXPosition, prizeYPostion))
    
    pygame.display.flip()

    for event in pygame.event.get():
#if user desides to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
#Test if the key pressed is the one we want.
        if event.type == pygame.KEYDOWN: #if the key is pressed 

            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        if event.type == pygame.KEYUP: #if the key is not pressed 

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
#move the player in a direction according to the key pressed, using co-ordinates of the Y,X axis.
    if keyUp == True:
        if playerYPosition > 0 :
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        playerXPosition -= 1
    if keyRight == True:
        playerXPosition += 1    

#create a box around the player, enemies and prize
    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    prizeBox = pygame.Rect(prize.get_rect())
    
    prizeBox.top = prizeYPostion
    prizeBox.left = prizeXPosition
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition 
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
        
#If the players box collide, the user either wins or losses(deoending on which box) and the game ends.
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box): 

        print("You lose!")

        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox): 

        print("You win!")

        pygame.quit()
        
        exit(0)
#To make the enemies move across the screen 
    enemyXPosition -= 0.15
    enemy2XPosition -= 0.30 
    enemy3XPosition -= 0.20 