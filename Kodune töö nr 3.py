# ÜL 3.5
from datetime import *
failinimi = input("Palun sisestage failinimi(nimekiri.txt): ")
fail = open(failinimi, encoding="UTF-8")
nimed = []

for rida in fail:
    nimed.append(rida)
fail.close()

print ("Vastama tuleb: ",nimed[(datetime.now().day)-1],end="")


#Ül 3.4
automaat = input("jukebox.txt\n 80ndad.txt\n eesti_muusika.txt\n edm.txt\n Palun sisestage failinimi: ")
failinimi = open(automaat, encoding="UTF-8")
laulud = []
number = 0
for i in fail:
    laulud.append(i)
    number+=1
    print (number,".",i)
    
fail.close()

laul = int(input("\n\nValige laulu järjekorranumber: "))
print(laulud[laul-1])

#Ül 3.3

fail = open("konto.txt", encoding="UTF-8")
sissetulek = []
for rida in fail:
    if float(rida)>0:
        sissetulek.append(float(rida))
fail.close()

for i in sissetulek:
    print(i)
    



#Ül 3.1

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
    
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
valik = vastuvõetud[aastad.index(aasta)]
print(aasta, "aastal oli vastuvõetud", valik)



#Ül 3.2

ringid = int(input("Sisesta ringide arv: "))
porgandid = 0
for i in range(1,ringid+1):
    if i%2==0:
        porgandid+=i
print("Saadavate porgandite koguarv on " + str(porgandid))