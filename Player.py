import pygame
import time
import random


class player():
    def __init__(self, screen, Color, Window, ground):
        self.Window = (Window[0], Window[1]-ground)
        self.dimensions = (20, 50)
        self.pos = [self.dimensions[0], self.Window[1]-self.dimensions[1]]
        self.screen = screen
        self.Color = Color
        self.HeadColor = Color
        self.arm = -1
        self.impulse = -1000000
        self.b = False
        self.Crashed = 5
        self.separate = True
        self.died = False
        self.font =  pygame.font.Font('AnyFont.ttf', 32)

    def DrawHead(self):
        self.HeightHead = self.dimensions[0]
        self.WidthHead = self.dimensions[0]
        if not self.died:
            if not self.b:
                pygame.draw.ellipse(self.screen, self.HeadColor, (self.pos[0], self.pos[1], self.WidthHead, self.HeightHead))
            else:
                pygame.draw.ellipse(self.screen, self.HeadColor, (self.pos[0], self.pos[1]+20, self.WidthHead, self.HeightHead))
        else:
            pygame.draw.ellipse(self.screen, self.HeadColor, (self.Window[0]//2-self.WidthHead//2, self.Window[1]-self.HeightHead, self.WidthHead, self.HeightHead))

    def DrawBody(self):
        self.heightBody = self.dimensions[1]*3//4-self.HeightHead
        self.endBody = (self.pos[0] + self.dimensions[0]//2, self.pos[1]+self.HeightHead+self.heightBody)
        if not self.b:
            pygame.draw.line(self.screen, self.Color, (self.pos[0] + self.dimensions[0]//2, self.pos[1]+self.HeightHead), self.endBody, self.WidhtBody)

    def DrawLegs(self):
        self.heightLeg = self.dimensions[1]//4
        pygame.draw.line(self.screen, self.Color, self.endBody, (self.pos[0], self.pos[1]+self.dimensions[1]), self.WidhtBody)#Left
        pygame.draw.line(self.screen, self.Color, self.endBody, (self.pos[0]+self.dimensions[0], self.pos[1]+self.dimensions[1]), self.WidhtBody)#Right

    def DrawArms(self):
        if self.b:
            k = 0
            l = 10
        else:
            if self.arm == 1:
                k = -10
                l = 0 #Visual illusion
            elif self.arm == -1:
                k = 10
                l = -5 #Visual illusion
            else:
                print("Invalid value for arm")
        self.BeginArm = (self.endBody[0], self.endBody[1]-self.heightBody//2 + l)
        pygame.draw.line(self.screen, self.Color, self.BeginArm, (self.pos[0], self.BeginArm[1]+k), self.WidhtBody)#Left
        pygame.draw.line(self.screen, self.Color, self.BeginArm, (self.pos[0] + self.dimensions[0], self.BeginArm[1]+k), self.WidhtBody)#Right

    def Draw(self, widhtBody=2):
        self.Move()
        self.Crash()
        self.WidhtBody = widhtBody
        self.DrawHead()
        self.DrawBody()
        self.DrawArms()
        self.DrawLegs()

    def Move(self):
        if self.impulse > -26:
            if self.impulse > 0:
                self.pos[1] -= 2
                self.arm = 1
            elif self.impulse < 0:
                self.pos[1] += 2
                self.arm = -1
            self.impulse -= 1

    def Jump(self):
        if self.pos[1] == self.Window[1]-self.dimensions[1] and not self.b:#Is on the ground?
            self.impulse = 25

    def Bend(self):
        if self.pos[1] == self.Window[1]- self.dimensions[1]:#Is on the ground?
            if not self.b:
                self.b = True
            else:
                self.b = False

    def RightLeft(self, direction):#Direction can be +1 or -1
        if direction > 0:
            if not self.pos[0]+self.dimensions[0] >= self.Window[0]:
                self.pos[0] += 2
                self.separate = True
            else:
                if self.separate:
                    self.Crashed -= 1
                    self.separate = False
        elif direction < 0:
            if not self.pos[0] <= 0:
                self.pos[0] -= 2
                self.separate = True
            else:
                if self.separate:
                    self.Crashed -= 1
                    self.separate = False

    def Crash(self):
        if self.Crashed <= 0:
            self.HeadColor = (255, 0, 0)

    def Die(self):
        self.HeadColor = (255, 0, 0)
        self.animation()

    def animation(self):
        x = 0
        while True:
            if x > 375:
                self.died = True
                break
            pygame.draw.circle(self.screen, (0,0,0), (self.Window[0]//2, self.Window[1]//2), x)
            game_over = self.font.render("GAME OVER", True, (255, 255, 255))
            self.screen.blit(game_over, (self.Window[0]//2-100, self.Window[1]//2-16))
            x += 1
            pygame.display.update()
            time.sleep(0.01)
            
