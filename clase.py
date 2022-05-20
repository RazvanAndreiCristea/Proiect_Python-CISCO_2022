from turtle import Turtle

class Judet(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.nume_judet = "substituent"
        self.numar_judet = -1
        self.pozitie = (0, 0)

    def scrie_numar(self):
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(self.pozitie)
        self.write(self.numar_judet, align = "center")

    def scrie_judet(self):
        self.clear()
        self.color("green")
        self.write(self.nume_judet, align = "center")

    def gresala_judet(self):
        self.clear()
        self.color("red")
        self.write(self.nume_judet, align = "center")