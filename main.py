import pygame
import time
import random
from Player import player
import enemies

width = 500
height = 500
groundHeight = 50
direction = 0
difficult = 1
instructions = True
running = True
en = ["Spike", "Square", "Rect"]
milisec = 0
score = -1

#Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DGRAY = (200, 200, 200)
GRAY = (100, 100, 100)
colors = [RED, GREEN, BLUE, BLACK, DGRAY, GRAY]
c = 0

pygame.init()
w = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hack from home")

font = pygame.font.Font('AnyFont.ttf', 32)
fontB = pygame.font.Font('Black Hold.ttf', 32)
littleFont = pygame.font.Font('Black Hold.ttf', 16)
Me = player(w, BLUE, (width, height), groundHeight)
MyEnemies = []

def DrawScore(score, font):
    score = font.render("Score: "+str(score), True, BLACK)
    w.blit(score, (width//2-50, 0))

while instructions:
    w.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            instructions = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
                instructions = False
            elif event.key == pygame.K_SPACE:
                instructions = False

    rules = fontB.render("Use the arrow keys to move to", True, WHITE)
    rules2 = fontB.render("the left, right, jump or bend", True, WHITE)
    follow = littleFont.render("Press space to start", False, WHITE)
    w.blit(rules, (width//2-200, height//2-32))
    w.blit(rules2, (width//2-200, height//2))
    w.blit(follow, (width//2-100, height-16))
    pygame.display.update()

while running:
    if milisec % 1000 == 0:
        for i in range(difficult):
            c += 1
            if c == len(colors):
                c = 0
            y = random.randint(1, 2)
            x = random.randint(0, len(en)-1)
            if y == 1:
                MyEnemies.append(enemies.UpEnemy(colors[c], (width, height), w, en[x]))
            else:
                MyEnemies.append(enemies.DownEnemy(colors[c], (width, height), w, en[x]))

    if milisec % 2000 == 0:
        score += 1
        done = False
    
    if score % 20 == 0 and score != 0:
        if not done:
            difficult += 1
            done = True

    if Me.died:
        running = False
    w.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
            elif event.key == pygame.K_UP:
                Me.Jump()
            elif event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_LEFT:
                direction = -1
            elif event.key == pygame.K_DOWN:
                Me.Bend()
            elif event.key == pygame.K_ESCAPE:
                Me.Die()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                direction = 0
            elif event.key == pygame.K_DOWN:
                Me.Bend()

    pygame.draw.rect(w, (GRAY[0]+5, GRAY[1]+5, GRAY[2]+5), (0, width-groundHeight, width, groundHeight))
    for x in MyEnemies:
        x.Move()
        x.Draw()
        if x.Kill(Me.pos, Me.dimensions):
            if not Me.died:
                Me.Die()
                score = ""
                break
        x.CheckDeath()
        if x.died:
            MyEnemies.remove(x)
    Me.RightLeft(direction)
    Me.Draw()
    DrawScore(score, font)
    pygame.display.update()
    time.sleep(0.01)
    milisec += 10
