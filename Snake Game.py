#IMPORTS 
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#CREATING SCREEN
window = Screen()
window.setup(600, 600)
window.bgcolor('black')
window.title('Snake Game !')
window.tracer(0)

#CREATING OBJECTS
snake = Snake()
food = Food()
score = Score()

#MAIN GAME
def make_game_false():
    global game
    game = False
    
game = True
while game:
    snake.move()
    window.update()
    time.sleep(0.05)

    #CHECK USER KEYBOARD CLICKS
    window.listen()
    window.onkey(snake.up , 'Up')
    window.onkey(snake.down , 'Down')
    window.onkey(snake.left , 'Left')
    window.onkey(snake.right , 'Right')
    window.onkey(make_game_false , 'Escape')

    #CHECK TO EAT
    if snake.head.distance(food) < 15 :
        food.appear()
        snake.extend()
        score.increase()
        continue

    #CHECK IF IT HAS TOUCHED THE EDGE
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280) or (snake.head.ycor() > 280 or snake.head.ycor() < -280):
        score.game_over()
        game = False
        
    #CHECK IF IT HAS TOUCHED ITS BODY
    for block in snake.turtles[:-1]:
        if snake.head.distance(block) < 5:
            score.game_over()
            game = False

window.exitonclick()