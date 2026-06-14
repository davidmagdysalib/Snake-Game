from turtle import Turtle

class Snake():
    """
    The Class That Creates, Extends and Move Snake In Any Direction
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        self.turtles = []
        self.positions = [(-20,0), (0,0), (20,0)]
        self.create_snake()
        self.head = self.turtles[-1]

    def create_snake(self):
        """
        Create Snake Method
        """
        for i in range(len(self.positions)):
            block = Turtle("square")
            block.shapesize(0.5 ,0.5)
            block.color('white')
            block.penup()
            block.goto(self.positions[i])
            self.turtles.append(block)

    def extend(self):
        """
        Extend Snake Method
        """
        
        block = Turtle('square')
        block.shapesize(0.5,0.5)
        block.color('white')
        block.penup()
        block.goto(self.turtles[0].pos())
        self.turtles.insert(0, block)

    def move(self):
        """
        Move Snake Methd
        """
        
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(  self.turtles[i+1].pos() )
        self.head.forward(10)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)