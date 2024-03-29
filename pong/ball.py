from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
    def move(self):
        new_x=self.xcor() + self.x_move
        new_y=self.ycor() +self.y_move
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.y_move *=-1
    
    def hit_paddle(self):
        self.x_move*=-1
    def reretpos(self):
        self.goto(0,0)
        self.hit_paddle()