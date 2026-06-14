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
        self.highscore = self.get_highscore()
        self.display()

    def display(self):
        """
        Display Method
        """
        
        self.goto(0, 250)
        self.write(f"Score :\n     {self.score}", align = "center", font = ('arial', 12, "bold"))
        self.goto(-230, 280)
        self.write(f"High score : {self.highscore}" , align = "center", font = ('arial', 12, "bold"))
        
    def increase(self):
        """
        Increase Score Method
        """
        
        self.score += 1
        if self.score > self.highscore :
            self.highscore = self.score
            self.save_highscore()
        self.clear()
        self.display()

    def game_over(self):
        """
        Game Over Method
        """
        
        self.goto(0,0)
        self.screen.bgcolor("dark red")
        self.clear()
        if self.score > self.highscore :
            self.highscore = self.score
            self.save_highscore()
        self.write(f"==============Game Over==============\n\n       Final Score : { self.score}\n\n       HighScore : {self.highscore}", align = "center", font = ('arial', 10, "bold"))

    def get_highscore(self):
        """
        Getting High Score Through A Method

        Returns:
            _type_: _description_
        """
        
        with open("./Python/OctuCode/OctuCode (00-2)/3,4- Snake Game/Snake Game/score.txt", "r") as file:
            return int(file.read())
        
    def save_highscore(self):
        """
        Saving New Highscore Through A Method
        """
        
        with open("./Python/OctuCode/OctuCode (00-2)/3,4- Snake Game/Snake Game/score.txt", "w") as file:
            file.write(str(self.highscore))
            
    def reset(self):
        """
        Reseting Highscore through a Method
        """
        with open("./Python/OctuCode/OctuCode (00-2)/3,4- Snake Game/Snake Game/score.txt", "w") as file:
            file.write(str(0))