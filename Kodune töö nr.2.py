 #2.1 bussid
print("Sisesta reisijate arv:")
reisijad = int(input())
print("Sisesta bussi kohtade arv:")
kohad = int(input())
bussitäis = int(reisijad) // int(kohad)
jääk = int(reisijad) % int(kohad)
if jääk > 0:
    bussitäis = bussitäis + 1
else:
        jääk= int(reisijad) // bussitäis
print("Busside vajadus" + str(bussitäis))
print("Viimases bussis inimesi" + str(jääk))

buss = reisijad // kohad
jääk = reisijad % kohad



#2.3Murelikud lapsevanemad
print("Sisesta ringide arv:")
ringid = input()
ringid = int(ringid)
i=2
summa = 0
while i<= ringid:
 summa += i
 i += 2
print("Porgandite koguarv on " + str(summa))    
        
#2.2  Äratus     
äratus= input("Siseta palun mitu korda äratus heliseb:")
äratus= int(äratus)
for i in range(0,äratus):
            print("Tõuse ja sära")


print("Tere"*3)