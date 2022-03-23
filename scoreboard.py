from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('Red')
        self.penup()
        self.hideturtle()

        self.goto(x=0, y=275)
        self.write(arg=f'Score={self.score}', move=True, align='Right', font=('ComicSans', 15, 'normal'))

    def score_refresh(self):
        self.write(arg=f'Score={self.score}', move=True, align='Right', font=('ComicSans', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_refresh()
    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg=f'GAME OVER', move=True, align='Center', font=('ComicSans', 40, 'normal'))

