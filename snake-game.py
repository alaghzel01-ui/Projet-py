import turtle
import random
import time

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()


# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


# Snake body
segments = []
score = 0


# Obstacles
obstacles = []
obstacle_positions = [(0, 0), (60, 0), (-60, 0), (0, 60), (0, -60)]

for pos in obstacle_positions:
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("orange")
    obstacle.penup()
    obstacle.goto(pos)
    obstacles.append(obstacle)


# Game Over text
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.color("white")
game_over.penup()


# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "normal"))


# Movement
def go_up():
    snake.setheading(90)


def go_down():
    snake.setheading(270)


def go_left():
    snake.setheading(180)


def go_right():
    snake.setheading(0)


# Keyboard
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


def reset_game():
    global segments, score

    snake.goto(-150, -150)
    snake.setheading(0)

    for segment in segments:
        segment.hideturtle()
    segments = []

    score = 0
    score_display.clear()
    score_display.write("Score: 0", align="center", font=("Arial", 16, "normal"))

    food.goto(0, 100)
    game_over.clear()

    main_loop()


def main_loop():
    global score

    while True:

        # Move body
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # First segment follows head
        if len(segments) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y)

        # Move snake
        snake.forward(4)

        # Snake position
        x = snake.xcor()
        y = snake.ycor()

        # Wall collision
        game_ended = False

        if x > 290 or x < -290 or y > 290 or y < -290:
            game_ended = True

        # Obstacle collision
        for obstacle in obstacles:
            if snake.distance(obstacle) < 20:
                game_ended = True

        if game_ended:
            game_over.goto(0, -30)
            game_over.write(
                "GAME OVER!",
                align="center",
                font=("Arial", 30, "bold")
            )
            game_over.goto(0, -70)
            game_over.write(
                "Click to play again",
                align="center",
                font=("Arial", 16, "normal")
            )
            screen.update()
            screen.onclick(lambda x, y: reset_game())
            return

        # Eat food
        if snake.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            segments.append(new_segment)

            score += 1
            score_display.clear()
            score_display.write("Score: " + str(score), align="center", font=("Arial", 16, "normal"))

        # Update screen
        screen.update()
        time.sleep(0.015)


snake.goto(-150, -150)
main_loop()
screen.mainloop()