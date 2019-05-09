"""
Final Project: Breakout Game
Author: Sean
Credit: Tutorials
Assignment: Create an old-school Breakout game
"""

from ggame import App, RectangleAsset, CircleAsset, Sprite, LineStyle, Color
import math
import random

class Walls(Sprite):
    def __init__(self, position, asset):
        super().__init__(asset, position)
        
class Ceiling(Sprite):
    def __init__(self, position, asset):
        super().__init__(asset, position)
        
class Bricks(Sprite):
    black = Color(0, 1)
    noline = LineStyle(0, black)
        
class Ball(Sprite):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    circ = CircleAsset(5, noline, black)
    
    def __init__(self, position):
        super().__init__(Ball.circ, position)
        self.speed = 3
        self.vx = 0
        self.vy = self.speed
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class Paddle(Sprite):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    paddlewidth = 100
    rect = RectangleAsset(paddlewidth, 10, noline, black)
    
    def __init__(self, position, maxwidth):
        super().__init__(Paddle.rect, position)
        self.speed = 10
        self.vx = 0
        self.maxwidth = maxwidth
        
        BreakoutGame.listenKeyEvent("keydown", "right arrow", self.moveRightOn)
        BreakoutGame.listenKeyEvent("keyup", "right arrow", self.moveRightOff)
        BreakoutGame.listenKeyEvent("keydown", "left arrow", self.moveLeftOn)
        BreakoutGame.listenKeyEvent("keyup", "left arrow", self.moveLeftOff)
        
    def moveRightOn(self, event):
        self.vx = self.speed
        
    def moveRightOff(self, event):
        self.vx = 0
        
    def moveLeftOn(self, event):
        self.vx = -self.speed
        
    def moveLeftOff(self, event):
        self.vx = 0
        
    def step(self):
        if self.vx > 0 and self.x < self.maxwidth - 10 - self.width:
            self.x += self.vx
        elif self.vx < 0 and self.x > 10:
            self.x += self.vx
        else:
            self.vx = 0

class BreakoutGame(App):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    
    def __init__(self):
        super().__init__()
        self.lives = 3
        print("Lives: " + str(self.lives))
        
        # Create walls
        self.ceiling = RectangleAsset(self.width, 10, BreakoutGame.noline, BreakoutGame.black)
        self.wall = RectangleAsset(10, self.height, BreakoutGame.noline, BreakoutGame.black)
        
        self.ceiling = Ceiling((0, 0), self.ceiling)
        self.leftwall = Walls((0, 0), self.wall)
        self.rightwall = Walls((self.width - 10, 0), self.wall)
        
        # Create bricks
        self.brickwidth = (self.width - self.wall.width * 2 - 11 * 10) / 10
        self.brickasset = RectangleAsset(self.brickwidth, 25, BreakoutGame.noline, BreakoutGame.black)
        for row in range(0,6):
            for column in range(0,10):
                Bricks(self.brickasset, (30 + column * 110, row * 40 + 100))
        
        # Create player & ball
        self.player = Paddle((self.width / 2 - Paddle.paddlewidth / 2, self.height - 50), self.width)
        self.ball = Ball((self.width / 2, self.height* 2 / 3))
        
    def step(self):
        self.player.step()
        self.ball.step()
        
        # Ball bouncing off walls
        if self.ball.x < 10:
            self.ball.vx = -self.ball.vx
        elif self.ball.x > self.width - 20:
            self.ball.vx = -self.ball.vx
            
        # Ball bouncing off ceiling
        if self.ball.y < 10:
            self.ball.vy = -self.ball.vy
            
        # Ball bouncing off paddle
        if self.ball.collidingWithSprites(Paddle) and self.ball.y <= self.player.y:
            self.ball.vy = - self.ball.vy
            if self.ball.x < self.player.x + self.player.width / 4:
                self.ball.vy = self.ball.vy * math.sin(math.pi/2)
                self.ball.vx = self.ball.vy
            elif self.ball.x > self.player.x + self.player.width * 3 / 4:
                self.ball.vy = self.ball.vy * math.sin(math.pi/2)
                self.ball.vx = -self.ball.vy
        
        # Ball falling down past paddle
        if self.ball.y > self.height and self.lives > 0:
            self.ball.x = self.width/2
            self.ball.y = self.height/2
            self.ball.vx = 0
            self.ball.vy = self.ball.speed
            self.lives -= 1
            print("Lives: " + str(self.lives))
        elif self.ball.y > self.height:
            print("Game Over")
            self.ball.destroy()
            self.destroy()
        
myapp = BreakoutGame()
myapp.run()