#Meeri Seiman
#Kodutöö 1

print ("Tere, maailm!")


aasta = "2020"
liblikas = "teelehemosaiikliblikas"
lause_keskosa = "aastaliblikas"
lause = ['aasta','liblikas', 'lause_keskosa' ]
print("".join(lause))

import math

valueA = 4
valueB = 5
valueC = 8

aExp = valueA ** 2
bExp = valueB ** 2
cExp = valueC ** 2

print(valueA, "^2 = ", aExp, sep="")
print(valueB, "^2 = ", bExp, sep="")
print(valueC, "^2 = ", cExp, sep="")

#Tervitus
print ("Tere, maailm!")

#Aasta liblikas

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ".aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)

#Astendamine

alus = int(input("Sisestage astme alus: "))
astendaja = int(input("Sisestage astendaja: "))
aste = alus**astendaja
print(aste)

#Trahv

nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
trahv = min(190,(tegelik_kiirus-lubatud_kiirus)*3)
print(nimi+", kiiruse ületamise eest on teie trahv",trahv,"eurot")







