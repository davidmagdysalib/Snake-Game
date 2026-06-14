from turtle import Turtle

class Score(Turtle):
    """
    Score Class That Inherit From Turtle Class From Turtle Module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.display()

    def display(self):
        """
        Display Method
        """
        
        self.goto(0, 250)
        self.write(f"Score :\n     {self.score}", align = "center", font = ('arial', 12, "bold"))
        
    def increase(self):
        """
        Increase Score Method
        """
        
        self.score += 1
        self.clear()
        self.display()

    def game_over(self):
        """
        Game Over Method
        """
        
        self.goto(0,0)
        self.screen.bgcolor("dark red")
        self.clear()
        self.write(f"==============Game Over==============\n\n       Final Score : { self.score}\n\n ", align = "center", font = ('arial', 10, "bold"))
