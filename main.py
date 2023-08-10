import tkinter
from snake import Snake
from turtle import Screen
import time
from food import Food
from score import ScoreBoard
from tkinter import Tk, Label, Button, PhotoImage

import ctypes
my_app = 'mycompany.myproduct.subproduct.version'   # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app)


window = Tk()
window.geometry('850x542')
window.resizable(False,False)           # make window fixed size
window.title("Snake Game")
bg = PhotoImage(file="ka.gif")

label1 = Label(window, image=bg)
label1.place(x=0, y=0)

label = Label(window, text="Welcome to Snake Game Press Play to start the game", fg="cyan", bg="black",
              font=("Cairo", 16, "bold"))
label.pack(side=tkinter.TOP, pady=5)


def start_game():
    window.destroy()
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


b = Button(window, text="Play", command=start_game, height=3, width=10, font=("Cairo", 16, "bold"),
           fg="yellow", bg="black")

b.pack(side=tkinter.BOTTOM, pady=30)

window.iconbitmap('snake.ico')
window.mainloop()
