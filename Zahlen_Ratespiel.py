# Spiel Zufallszahlen

from random import *

zahl = 0.0
ergebnis = 25
weiterspielen = True
zufalls_zahl = randint(1, 40)

while weiterspielen:
    zahl = int(input("Geben Sie eine Zahl ein!\n"))

    if zahl < zufalls_zahl:
        print("Zahl zu niedrig!")
    elif zahl == zufalls_zahl:
        print("Gewonnen!")
        break
    else:
        print("Zahl zu hoch!")
