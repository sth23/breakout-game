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
    black = Color(0, 1)
    noline = LineStyle(0, black)
    
    def __init__(self, asset, position):
        super().__init__(asset, position)

class BreakoutGame(App):
    def __init__(self):
        super().__init__()
        
        # Create walls
        self.black = Color(0, 1)
        self.noline = LineStyle(0, black)
        self.ceiling = RectangleAsset(self.width, 10, self.noline, self.black)
        self.wall = RectangeAsset(10, self.height, self.noline, self.black)
        
        Walls((0, 0), self.ceiling)
        Walls((0, 0), self.wall)
        Walls((self.width - 10, 0), self.wall)
        
myapp = BreakoutGame()
myapp.run()