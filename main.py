import turtle
import pandas
import winsound
from random import choice as noroc
from random import randint as alegere
from time import sleep as adormire
from tkinter import messagebox as fereastra_informativa
from judetu import Judet
from orasu import Oras
from titlu import Titlu

ecran = turtle.Screen()
ecran.title("Câștigă România învățând care sunt județele și reședințele de județ ale acestora")
ecran.bgcolor("black")

screen_width = turtle.getcanvas().winfo_screenwidth()
screen_height = turtle.getcanvas().winfo_screenheight()

harta = "romania.gif"
ecran.addshape(harta)
turtle.shape(harta)
ecran.setup(width=screen_width, height=screen_height)

titlu = Titlu()

winsound.PlaySound('Ta-daaa.wav', winsound.SND_FILENAME)

coordonate_judete = pandas.read_csv("coordonate_judete.csv")

lista_judete = coordonate_judete["judet"].to_list()
x_lista = coordonate_judete["x"].to_list()
y_lista = coordonate_judete["y"].to_list()

coordonate_orase = pandas.read_csv("coordonate_orase.csv")

lista_orase = coordonate_orase["orase"].to_list()
x1_lista = coordonate_orase["x"].to_list()
y1_lista = coordonate_orase["y"].to_list()

dictionar_judete = {}
dictionar_orase = {}

for j in range(len(lista_judete)):
    tuplu = (x_lista[j], y_lista[j])
    dictionar_judete[lista_judete[j]] = tuplu

for j in range(len(lista_orase)):
    tuplu1 = (x1_lista[j], y1_lista[j])
    dictionar_orase[lista_orase[j]] = tuplu1

adormire(1)
fereastra_informativa.showinfo("Mesaj cu titlu informativ.", "Județele sunt scrise fără diacritice și fără cratimă (ex: Bistrita-Nasaud => Bistrita Nasaud. Literele inițiale pot fi scrise cu litera mare sau mică (restul literelor trebuie scrise doar cu litera mică). "
                                   "Pentru a încheia programul mai devreme introduceți cuvântul 'gata'. Acelasi lucru este valabil și pentru reședințele de județ. Spor la joc!")

winsound.PlaySound('Play_game.wav', winsound.SND_FILENAME)

total_judete = len(lista_judete)
total_orase = len(lista_orase)

judete_obiectuale = []
orase_obiectuale = []

judete_corecte_gresite = []
orase_corecte_gresite = []

def creare():

    global judete_obiectuale, orase_obiectuale

    index_judete = []
    index_orase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for j in range(total_judete):
        index_judete.append(j + 1)

    for j in range(total_judete):

        judetel = Judet()

        index_judet = noroc(index_judete)
        judetel.nume_judet = lista_judete[j]
        judetel.numar_judet = index_judet
        index_judete.remove(index_judet)
        judetel.pozitie = dictionar_judete[lista_judete[j]]

        judete_obiectuale.append(judetel)
        judetel.scrie_numar()

        orasel = Oras()

        index_oras = noroc(index_orase)
        orasel.nume_oras = lista_orase[j]
        orasel.litera_oras = index_oras
        index_orase.remove(index_oras)
        orasel.pozitie = dictionar_orase[lista_orase[j]]

        orase_obiectuale.append(orasel)
        orasel.scrie_litera()

def stergere():

    global judete_obiectuale
    global orase_obiectuale
    global judete_corecte_gresite
    global orase_corecte_gresite

    for judet in judete_corecte_gresite:
        judet.clear()

    for oras in orase_corecte_gresite:
        oras.clear()

    judete_corecte_gresite.clear()
    orase_corecte_gresite.clear()

    for judet in judete_obiectuale:
        judet.clear()

    for oras in orase_obiectuale:
        oras.clear()

    judete_obiectuale.clear()
    orase_obiectuale.clear()

def joculet():

    global judete_obiectuale
    global orase_obiectuale

    judete_ghicite = 0
    orase_ghicite = 0
    numar_judete_corecte = 0
    numar_orase_corecte = 0

    while judete_ghicite < total_judete or orase_ghicite < total_orase:

        randomizare = -1

        if judete_ghicite == total_judete:
            randomizare = 2

        elif orase_ghicite == total_orase:
            randomizare = 1

        else:
            randomizare = alegere(1, 2)

        if randomizare == 1:
            judet_selectat = noroc(judete_obiectuale)
            judet_selectat.judet_curent()
            raspuns = ecran.textinput(title = f"Ești la întrebarea {judete_ghicite + 1} din {total_judete}", prompt = f"Numele județului cu numărul {judet_selectat.numar_judet} este: ")

            if raspuns is None:
                break

            elif raspuns is not None:
                     raspuns = raspuns.title()

            if raspuns == "Gata":
                for obiect_judet in judete_obiectuale:
                    obiect_judet.gresala_judet()
                
                judete_ghicite = total_judete

            elif raspuns == judet_selectat.nume_judet: 
                judet_selectat.scrie_judet() 
                winsound.PlaySound('Raspuns_corect.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)
                judete_corecte_gresite.append(judet_selectat) 
                judete_obiectuale.remove(judet_selectat) 
                judete_ghicite += 1 
                numar_judete_corecte += 1
                

            else:
                judet_selectat.gresala_judet()
                winsound.PlaySound('Raspuns_gresit.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)
                judete_corecte_gresite.append(judet_selectat)
                judete_obiectuale.remove(judet_selectat)
                judete_ghicite += 1

        elif randomizare == 2:
            oras_selectat = noroc(orase_obiectuale)
            oras_selectat.oras_curent()
            raspuns = ecran.textinput(title = f"Ești la întrebarea {orase_ghicite + 1} din {total_orase}", prompt = f"Numele orașul cu litera {oras_selectat.litera_oras} este: ")

            if raspuns is None:
                break

            elif raspuns is not None:
                     raspuns = raspuns.title()

            if raspuns == "Gata":
                for obiect_oras in orase_obiectuale:
                    obiect_oras.gresala_oras()

                orase_ghicite = total_orase

            elif raspuns == oras_selectat.nume_oras:
                oras_selectat.scrie_oras()
                winsound.PlaySound('Raspuns_corect.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)
                orase_corecte_gresite.append(oras_selectat)
                orase_obiectuale.remove(oras_selectat)
                orase_ghicite += 1
                numar_orase_corecte += 1

            else:
                oras_selectat.gresala_oras()
                winsound.PlaySound('Raspuns_gresit.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)
                orase_corecte_gresite.append(oras_selectat)
                orase_obiectuale.remove(oras_selectat)
                orase_ghicite += 1
    
    if numar_judete_corecte != 0 or numar_orase_corecte != 0:
        fereastra_informativa.showinfo("Joc încheiat", f"Felicitări ai identificat corect {numar_judete_corecte} județe si {numar_orase_corecte} reședințe de județ pe harta României din totalul de {total_judete} de județe și {total_orase} de reședințe!")

    elif numar_judete_corecte == total_judete and numar_orase_corecte == total_orase:
        fereastra_informativa.showinfo("Joc încheiat", "Felicitări ai identificat corect toate județele României. Ești un zeu al geografiei!")

    else:
        fereastra_informativa.showinfo("Joc încheiat", f"Frate nu știi deloc geografia României punctajul tău este {numar_judete_corecte + numar_orase_corecte} ")

creare()

jocul_merge = True
adormire(1)
fereastra = fereastra_informativa.askquestion("Start", "Ești gata să câștigi România?")

if fereastra == "no":
    jocul_merge = False

if jocul_merge == True:

   joculet()

   reincercare = fereastra_informativa.askyesno("Replay", "Apasă pe da dacă vrei să mai joci din nou!")

   if reincercare == False:
    fereastra_informativa.showwarning("Program încheiat", "Aici se incheie jocul tau, ne mai vedem alta data!")
    ecran.bye()

   while reincercare:
       stergere()
       adormire(1)
       creare()
       joculet()
       reincercare = fereastra_informativa.askyesno("Replay", "Apasă pe da dacă vrei să mai joci din nou!")

       if reincercare == False:
        fereastra_informativa.showwarning("Program încheiat", "Aici se incheie jocul tau, ne mai vedem alta data!")
        ecran.bye()

else: 
    fereastra_informativa.showwarning("Avertisment", "Program încheiat!")
    ecran.bye()

if jocul_merge == True:
    turtle.mainloop()