from snake import Snake
from turtle import Screen
import time
from food import Food
from score import ScoreBoard


screen = Screen()
screen.bgpic("snake.gif")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()   # object from snake
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extended_snake()
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -290:
        game_is_on = False
        screen.reset()
        score.end_game()

    for square in snake.new_box[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            screen.reset()
            score.end_game()

screen.exitonclick()
