from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Up", fun=snake.up)

while game_on:
    screen.update()
    time.sleep(.1)
    snake.movement()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset1()
            snake.reset()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset1()
        snake.reset()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.add_segment()
        print(scoreboard.score)


scoreboard.reset1()
screen.exitonclick()



