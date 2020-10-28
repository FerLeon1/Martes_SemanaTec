from turtle import *
import random
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insideFood(food):
    "Return True if food inside boundaries."
    return -150 < food.x < 150 and -150 < food.y < 150

def moveSnake():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colb)

    square(food.x, food.y, 9, colf)
    update()
    ontimer(moveSnake, 100)

def moveFood():
    "Move food randomly, always to one adjacent square"
    aimFood = vector(randrange(-10, 11, 10), randrange(-10, 11, 10))
    print(aimFood)
    print(food.x, food.y)
    food.move(aimFood)
    ontimer(moveFood, 500)

    if not insideFood(food):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

setup(420, 420, 300, 0)
coloresjuego = ['green', 'blue', 'yellow', 'purple', 'black']
colb = random.choice(coloresjuego)
print(colb)
colf = random.choice(coloresjuego)
print(colf)
while colb == colf:
    colf = random.choice(coloresjuego)
    print(colf)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
moveSnake()
moveFood()
done()
