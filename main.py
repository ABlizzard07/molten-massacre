import pygame
import math

pygame.init()

# Screen and Caption
screen = pygame.display.set_mode((1500,1000))
pygame.display.set_caption("Molten Massacre")

# Setting the Icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player 1
player1Img = pygame.image.load('tank.png')
player1X = 100
player1Y = 400
player1X_change = 0
player1Y_change = 0

# Player 2
player2Img = pygame.image.load('tank2.png')
player2X = 1332
player2Y = 400
player2X_change = 0
player2Y_change = 0

# Flame 1
flame1Img = pygame.image.load('flame.png')
flame1X = 200
flame1Y = 500
flame1X_change = 10
state_1 = "ready"

# Flame 2
flame2Img = pygame.image.load('flame.png')
flame2X = 1300
flame2Y = 500
flame2X_change = -10
state_2 = "ready"

def player1(x, y):
    screen.blit(player1Img, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

def fire1(x, y):
    global state_1
    state_1 = "fired"
    screen.blit(flame1Img, (x, y))

def fire2(x, y):
    global state_2
    state_2 = "fired"
    screen.blit(flame2Img, (x, y))

def collision1(player2X, player2Y, flameX, flameY):
    distance = math.sqrt(math.pow(player2X - flameX, 2) + math.pow(player2Y - flameY, 2))

    if distance < 25:
        return True
    else:
        return False

def collision2(player1X, player1Y, flameX, flameY):
    distance = math.sqrt(math.pow(player1X - flameX, 2) + math.pow(player1Y - flameY, 2))

    if distance < 25:
        return True
    else:
        return False

# Hitpoints
hp1 = 10
hp2 = 10
hp_font = pygame.font.SysFont('Consolas', 50)

# Game Timer
counter = 300
text = '5:00'
pygame.time.set_timer(pygame.USEREVENT, 1000)
time_font = pygame.font.SysFont('Consolas', 70)

# Game Loop
on = True 

while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

        if event.type == pygame.USEREVENT:
            counter -= 1
            
            if counter % 60 == 0:
                text = str(int(counter / 60)) + ":00"
            elif counter % 60 <= 9:
                text = str(int(counter // 60)) + ":0" + str(counter - 60 * (int(counter // 60)))
            else:
                text = str(int(counter // 60)) + ":" + str(counter - 60 * (int(counter // 60)))

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                player1Y_change = -1
            if event.key == pygame.K_a:
                player1X_change = -1
            if event.key == pygame.K_s:
                player1Y_change = 1
            if event.key == pygame.K_d:
                player1X_change = 1
            if event.key == pygame.K_SPACE:
                if state_1 == "ready":
                  flame1X = player1X  
                  flame1Y = player1Y
                  fire1(flame1X, flame1Y)
            
            if event.key == pygame.K_UP:
                player2Y_change = -1
            if event.key == pygame.K_LEFT:
                player2X_change = -1
            if event.key == pygame.K_DOWN:
                player2Y_change = 1
            if event.key == pygame.K_RIGHT:
                player2X_change = 1
            if event.key == pygame.K_RETURN:
                if state_2 == "ready":
                    flame2X = player2X
                    flame2Y = player2Y
                    fire2(flame2X, flame2Y)
        
        if event.type == pygame.KEYUP:
            if event.key == (pygame.K_w or pygame.K_s):
                player1Y_change = 0

            if event.key == (pygame.K_a or pygame.K_d):
                player1X_change = 0
            
            if event.key == (pygame.K_UP or pygame.K_DOWN):
                player2Y_change = 0

            if event.key == (pygame.K_LEFT or pygame.K_RIGHT):
                player2X_change = 0
    
    screen.fill((0, 0, 0))
    screen.blit(time_font.render(text, True, (255, 255, 255)), (700, 50))

    screen.blit(hp_font.render(str(hp1), True, (255, 255, 255)), (200, 50))
    screen.blit(hp_font.render(str(hp2), True, (255, 255, 255)), (1200, 50))

    player1(player1X, player1Y)
    player2(player2X, player2Y)

    # Player Movement
    player1X += player1X_change
    player1Y += player1Y_change
    player2X += player2X_change
    player2Y += player2Y_change

    if player1X <= 0:
        player1X = 0
    if player1X >= 436:
        player1X = 436
    if player1Y <= 100:
        player1Y = 100
    if player1Y >= 936:
        player1Y = 936
    
    if player2X <= 1000:
        player2X = 1000
    if player2X >= 1436:
        player2X = 1436
    if player2Y <= 100:
        player2Y = 100
    if player2Y >= 936:
        player2Y = 936

    # Flame Movement

    if flame1X >= 1500:
        flame1X = player1X
        flame1Y = player1Y
        state_1 = "ready"

    if state_1 == "fired":
        fire1(flame1X, flame1Y)
        flame1X += flame1X_change

    if flame2X <= 0:
        flame2X = player2X
        flame2Y = player2Y
        state_2 = "ready"

    if state_2 == "fired":
        fire2(flame2X, flame2Y)
        flame2X += flame2X_change

    # Collisions

    collide1 = collision1(player2X, player2Y, flame1X, flame1Y)
    collide2 = collision2(player1X, player1Y, flame2X, flame2Y)

    if collide1:
        flame1X = player1X
        flame1Y = player1Y
        state_1 = "ready"
        hp2 -= 10

    if collide2:
        flame2X = player2X
        flame2Y = player2Y
        state_2 = "ready"
        hp2 -= 10

    pygame.display.update() 


"""
import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 10, '10'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    # clock.tick(60) 
"""