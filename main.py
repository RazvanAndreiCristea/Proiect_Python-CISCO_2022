import turtle, pandas
from random import choice as bulan
from time import sleep as dormi
from tkinter import messagebox as ferestruica
from judetu import Judet
from titlu import Titlu

ecran = turtle.Screen()
ecran.title("Câștigă România învățând care sunt județele acesteia")
ecran.bgcolor("black")

harta = "harta.gif"
ecran.addshape(harta)
turtle.shape(harta)

titlu = Titlu()

coordonate = pandas.read_csv("coordonate.csv")

lista_judete = coordonate["judet"].to_list()
x_lista = coordonate["x"].to_list()
y_lista = coordonate["y"].to_list()

dictionar_judete = {}

for j in range(len(lista_judete)):
    tuplu = (x_lista[j], y_lista[j])
    dictionar_judete[lista_judete[j]] = tuplu


dormi(1)
ferestruica.showinfo("Mesaj cu titlu informativ.", "Județele sunt scrise fără diacritice și fără cratimă (ex: Bistrita-Nasaud => Bistrita Nasaud. Literele inițiale pot fi scrise cu litera mare sau mică (restul literelor trebuie scrise doar cu litera mică). "
                                   "Pentru a încheia programul mai devreme introduceți cuvântul 'gata'.")

total_judete = len(lista_judete)
judete_obiectuale = []
index_judete = []

for j in range(total_judete):
    index_judete.append(j + 1)

for j in range(total_judete):

    judetel = Judet()
    index_judet = bulan(index_judete)
    judetel.nume_judet = lista_judete[j]
    judetel.numar_judet = index_judet
    index_judete.remove(index_judet)
    judetel.pozitie = dictionar_judete[lista_judete[j]]

    judete_obiectuale.append(judetel)
    judetel.scrie_numar()

jocul_merge = True
dormi(1)
fereastra = ferestruica.askquestion("Start", "Ești gata să câștigi România?")

if fereastra == "no":
    jocul_merge = False


if jocul_merge == True:

    numar_ghiciri = 0
    numar_judete_corecte = 0

    while numar_ghiciri < total_judete:
        judet_selectat = bulan(judete_obiectuale)
        judet_selectat.judet_curent()
        raspuns = ecran.textinput(title = f"Ești la întrebarea {numar_ghiciri + 1} din {total_judete}", prompt = f"Numele județului cu numărul {judet_selectat.numar_judet} este: ")

        if raspuns is None:
            break

        elif raspuns is not None:
                 raspuns = raspuns.title()

        if raspuns == "Gata":
            for obiect in judete_obiectuale:
                obiect.gresala_judet()

            break

        elif raspuns == judet_selectat.nume_judet:
            judet_selectat.scrie_judet()
            judete_obiectuale.remove(judet_selectat)
            numar_ghiciri += 1
            numar_judete_corecte += 1

        else:
            judet_selectat.gresala_judet()
            judete_obiectuale.remove(judet_selectat)
            numar_ghiciri += 1
    
    if numar_judete_corecte != 0:
        ferestruica.showinfo("Program încheiat", f"Felicitări identificat corect {numar_judete_corecte} județe corecte pe harta României din totalul de {total_judete} de județe!")

    elif numar_judete_corecte == total_judete:
        ferestruica.showinfo("Program încheiat", "Felicitări ai identificat corect toate județele României. Ești un zeu al geografiei!")

    else:
        ferestruica.showinfo("Program încheiat", f"Frate nu știi deloc geografia României punctajul tău este {numar_judete_corecte}")

else: 
    ferestruica.showinfo("Avertisment", "Program încheiat!")
    ecran.bye()

if jocul_merge == True:
    turtle.mainloop()