from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

scoreboard = Score()
screen = Screen()

screen.title(titlestring="SNAKE GAME")
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
game_on = True
snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, "Left")

while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move_snake()
    # detect Collision with food using Distance Class
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -299 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False
    #Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            scoreboard.game_over()
            game_on=False

    #detect when the Head collides with any Segment

screen.exitonclick()
