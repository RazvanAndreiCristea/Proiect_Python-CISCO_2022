from turtle import Turtle

class Titlu(Turtle):

	def __init__(self):
		super().__init__()
		self.speed("fastest")
		self.hideturtle()
		self.penup()
		self.goto(0, 400)
		self.color("yellow")
		self.write("Câștigă România!", font = ("Times New Roman", 28, "bold"), align = "center")