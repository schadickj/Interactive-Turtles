from turtle import Turtle 


class MoveingTurtle(Turtle):
  def __init__(self):
    Turtle.__init__(self)

    #initial setup
    self.shape("circle")
    self.shapesize(.5, .5, 1)

    #variables
    self.x_spd = 4