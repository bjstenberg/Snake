from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# Black background color
screen.bgcolor("black")
screen.title("Slithering snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
# Move the snake
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail
    #for shape in snake.shapes[1:]:
    #    if snake.head.distance(shape) < 10:
    #        scoreboard.reset()
    #    elif
    for shape in snake.shapes:
        if shape == snake.head:
            pass
        elif snake.head.distance(shape) < 10:
            scoreboard.reset()
            snake.reset()
            # if head collides with any segment in the tail, shape
        # trigger game_over


screen.exitonclick()
