from turtle import Turtle
from time import sleep

class Titlu(Turtle):

	def __init__(self):
		super().__init__()
		self.speed("slowest")
		self.hideturtle()
		self.penup()
		self.goto(-10, 400)
		self.color("yellow")
		self.write("Câștigă România", font = ("Times New Roman", 28, "bold"), align = "center")
		
		for i in range(10):
			self.clear()
			self.setx(self.xcor() + 4)
			self.write("Câștigă România", font = ("Times New Roman", 28, "bold"), align = "center")
			sleep(0.1)

		for i in range(10):
			self.clear()
			self.setx(self.xcor() - 4)
			self.write("Câștigă România", font = ("Times New Roman", 28, "bold"), align = "center")
			sleep(0.1)

		for i in range(10):
			self.clear()
			self.setx(self.xcor() - 4)
			self.write("Câștigă România", font = ("Times New Roman", 28, "bold"), align = "center")
			sleep(0.1)

		for i in range(10):
			self.clear()
			self.setx(self.xcor() + 4)
			self.write("Câștigă România", font = ("Times New Roman", 28, "bold"), align = "center")
			sleep(0.1)