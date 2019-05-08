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
        
class Paddle(Sprite):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    rect = RectangleAsset(50, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Paddle.rect, position)
        self.speed = 5
        self.vx = 0
        
        BreakoutGame.listenKeyEvent("keydown", "right arrow", self.moveRightOn)
        BreakoutGame.listenKeyEvent("keyup", "right arrow", self.moveRightOff)
        BreakoutGame.listenKeyEvent("keydown", "left arrow", self.moveLeftOn)
        BreakoutGame.listenKeyEvent("keyup", "left arrow", self.moveLeftOff)
        
    def moveRightOn(self, event):
        self.vx = -self.speed
        
    def moveRightOff(self, event):
        self.vx = 0
        
    def moveLeftOn(self, event):
        self.vx = -self.speed
        
    def moveLeftOff(self, event):
        self.vx = 0
        
    def step(self):
        self.x += self.vx

class BreakoutGame(App):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    
    def __init__(self):
        super().__init__()
        
        # Create walls
        self.ceiling = RectangleAsset(self.width, 10, BreakoutGame.noline, BreakoutGame.black)
        self.wall = RectangleAsset(10, self.height, BreakoutGame.noline, BreakoutGame.black)
        
        Walls((0, 0), self.ceiling)
        Walls((0, 0), self.wall)
        Walls((self.width - 10, 0), self.wall)
        
        self.player = Paddle((self.width/2, self.height - 20))
        
    def step(self):
        self.player.step()
        
myapp = BreakoutGame()
myapp.run()