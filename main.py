from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake')

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

food = Food()
scoreboard = Scoreboard()
snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_over = True
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            scoreboard.game_over()
            game_over = True


screen.exitonclick()
