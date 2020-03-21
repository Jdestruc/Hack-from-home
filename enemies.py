import pygame
import time
import random


class UpEnemy():
    def __init__(self, color, window, screen, tp):
        self.color = color
        self.window = window
        self.screen = screen
        self.tp = tp
        height = random.randint(5, 50)
        width = random.randint(5, 50)
        self.dimensions = (width, height)
        self.pos = [0, -height]
        self.pos[0] = random.randint(0, self.window[0]-self.dimensions[0])
        self.died = False

    def Draw(self):
        if self.tp == "Spike":
            pygame.draw.polygon(self.screen, self.color, ((self.pos[0], self.pos[1]), (self.pos[0]+self.dimensions[0]//2, self.pos[1]+self.dimensions[1]), (self.pos[0]+self.dimensions[0], self.pos[1])))
        elif self.tp == "Square":
            pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[0]))
        elif self.tp == "Rect":
            pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]))

    def Move(self):
        self.pos[1] += 1

    def CheckDeath(self):
        if self.pos[1] > self.window[1]:
            self.died = True
    
    def Kill(self, playerPos, playerSize):
        if self.AinB(playerPos, playerSize, self.pos, self.dimensions):
            return True

    def AinB(self, posA, sizeA, posB, sizeB):
        if (posA[0] > posB[0] and posA[0] < posB[0]+sizeB[0]) or (posA[0]+sizeA[0] > posB[0] and posA[0]+sizeA[0] < posB[0]+sizeB[0]):
            if (posA[1] > posB[1] and posA[1] < posB[1]+sizeB[1]) or (posA[1]+sizeA[1] > posB[1] and posA[1]+sizeA[1] < posB[1]+sizeB[1]):
                return True
            else:
                return False
        else:
            return False

class DownEnemy():
    def __init__(self, color, window, screen, tp):
        self.color = color
        self.window = window
        self.screen = screen
        self.tp = tp
        height = random.randint(0, 50)
        width = random.randint(0, 50)
        self.dimensions = (width, height)
        self.pos = [0, self.window[1]]
        self.pos[0] = random.randint(0, self.window[0])
        self.died = False

    def Draw(self):
        if self.tp == "Spike":
            pygame.draw.polygon(self.screen, self.color, ((self.pos[0], self.pos[1]+self.dimensions[1]), (self.pos[0]+self.dimensions[0]//2, self.pos[1]), (self.pos[0]+self.dimensions[0], self.pos[1]+self.dimensions[1])))
        elif self.tp == "Square":
            pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[0]))
        elif self.tp == "Rect":
            pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1]))
        
    def Move(self):
        if self.tp == "Spike":
            self.pos[1] -= 1

    def CheckDeath(self):
        if self.pos[1] > self.window[1]:
            self.died = True
    
    def Kill(self, playerPos, playerSize):
        if self.AinB(playerPos, playerSize, self.pos, self.dimensions):
            return True

    def AinB(self, posA, sizeA, posB, sizeB):
        if (posA[0] > posB[0] and posA[0] < posB[0]+sizeB[0]) or (posA[0]+sizeA[0] > posB[0] and posA[0]+sizeA[0] < posB[0]+sizeB[0]):
            if (posA[1] > posB[1] and posA[1] < posB[1]+sizeB[1]) or (posA[1]+sizeA[1] > posB[1] and posA[1]+sizeA[1] < posB[1]+sizeB[1]):
                return True
            else:
                return False
        else:
            return False