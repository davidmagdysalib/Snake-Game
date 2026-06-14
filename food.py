from turtle import Turtle
import random

class Food(Turtle):
    """
    Class Of Food That Inherit From Turtle Class From Turtle Module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.shape('circle')
        self.shapesize(0.25, 0.25)
        self.color('red')
        self.penup()
        self.appear()

    def appear(self):
        """
        Appear Food Method
        """
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)