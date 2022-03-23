import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.speed('fastest')
        self.shapesize(0.7)
        random_x=random.randint(-230, 230)
        random_y=random.randint(-230, 230)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(x=random_x, y=random_y)


