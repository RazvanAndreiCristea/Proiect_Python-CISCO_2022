from turtle import Turtle

class Oras(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.nume_oras = "substituent"
        self.litera_oras = ' '
        self.pozitie = (0, 0)

    def scrie_litera(self):
        self.color("dark green")
        self.hideturtle()
        self.penup()
        self.goto(self.pozitie)
        self.write(self.litera_oras, align = "center", font = ("Times New Roman", 12 , "bold"))

    def scrie_oras(self):
        self.clear()
        self.color("cyan")
        self.write(self.nume_oras, align = "center", font = ("Times New Roman", 10 , "bold"))

    def oras_curent(self):
        self.clear()
        self.color("magenta")
        self.write(self.litera_oras, align = "center", font = ("Times New Roman", 10 , "bold"))

    def gresala_oras(self):
        self.clear()
        self.color("brown")
        self.write(self.nume_oras, align = "center", font = ("Times New Roman", 10 , "bold"))