# 1. Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
import random
import re
from idlelib.replace import replace

print("1.---------------------------------------------------")
for i in range(10):
    print("labas")

# 2. Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
print("2.---------------------------------------------------")
for i in range(0,10): # atspausdina stulpeliu nuo 0 iki 9 imtinai
    print(i)

# 3. Sukurkite masyvą iš dešimties augalų pavadinimų.
print("3.---------------------------------------------------")
herbs = ["piene", "balanda", "asiuklis", "dilgele", "usnis", "varputis",
         "rugstyne", "saulute", "samana", "stumbrazole"]
print(herbs)

# 4. Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
print("4.---------------------------------------------------")
for herb in herbs: # atspausdina stulpeliu
    print(herb)

for i in range(len(herbs)): # suskaiciuoja kiek yra elementu ir atspausdina visus indeksus ir augalus stulpeliu
    print(f'i = {i}, herbs[{i}] = {herbs[i]}')

for i, herb in enumerate(herbs): # atspausdina visus indeksus ir augalus sarasu
    print(i, herb)

# 5. Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
print("5.---------------------------------------------------")
print(herbs[::-1])

# 6. Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
print("6.---------------------------------------------------")
print("---------------------------------------------------")
count = 0
for i in range(10, 51):
    if i % 2 == 0:
     print(i)
     count += 1
print(count)

print("---------------------------------------------------")
count = 0
for i in range(51)[10::2]:
    print(i)
    count += 1
print(count)

print("---------------------------------------------------")
count = 0
for i in range(10,51,2):
     print(i)
     count += 1
print(count)


# 7. Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.)
# (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
print("7.---------------------------------------------------")
count = 0
for i in range(10, 51):
    if i % 2 == 0:
     print(i)
     count += 1
print(count)
print("---------------------------------------------------")
count = 0
for i in range(10,51):
    if i % 10 == 0:
       continue
    count += 1
    print(i)
print(count)
print("---------------------------------------------------")
for i in range(10,51,2):
    if i % 10 == 0:
        continue
    count += 1
print(count)

# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20.
# Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
print("8.---------------------------------------------------")

count = 0
for i in range(0,20):
    #print(i)
    if i % 2 == 0:
        count += 1
print(count)

print("---------------------------------------------------")
count = 0
for i in range(0,20,2):
    print(i)
    count += 1
print(count)

# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
print("9.---------------------------------------------------")
print(herbs)
count = 0
for herb in herbs: # du identacijos lygiai. atspausdina visus augalus, kuriu ilgis mazesnis nei 5
    if len(herb) < 5 or len(herb) > 7:
        print(herb)
        count += 1
print(count)

print("---------------------------------------------------")
count = 0
for herb in herbs: # du identacijos lygiai. atspausdina visus augalus, kuriu ilgis mazesnis nei 5
    if len(herb) < 5 or len(herb) > 7:
        print(herb)
        count += 1
        print(count)
print("---------------------------------------------------")
count = 0
for herb in herbs: # du identacijos lygiai. atspausdina visus augalus, kuriu ilgis mazesnis nei 5
    if len(herb) < 5 or len(herb) > 7:
        print(herb)
        count += 1
    print(count)

# 10 Suskaičiuokite kiek 3čio uždavinio masyve yra
# žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
print("10.---------------------------------------------------")
count = 0
print(herbs)
for herb in herbs: # du identacijos lygiai. atspausdina visus augalus, kuriu ilgis (tarp 5 ir 10 simbolių ilgio)
    if len(herb) > 5 and len(herb) < 10:
        print(herb)
        count += 1
print(count)


# 1. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais vienoje eilutėje ir
# suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
print("1.S---------------------------------------------------")
count = 0
sk = 0
while True: # suka skaicius atsitiktinai
    dice = random.randint(0,300)
    #print(dice, end = " ")
    count += 1
    if count ==300:
        break
    if dice > 150:
        print(dice, end=" ")
        sk += 1
    # if dice > 275:
    #    print
print()
print(sk)
print("1.FIX---------------------------------------------------")

sk = 0
for i in range(300): # suka skaicius atsitiktinai
    dice = random.randint(0,300)
    if dice > 150:
        sk += 1
    if dice > 275:
        print(f'[{dice}]', end=" ")
    else:
        print(dice, end = " ")
print()
print(sk)

# 2. Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

print("2.S---------------------------------------------------")
count = 0
for i in range(1, 3000):
    if i % 77 == 0:
       count += 1
       print( f'{i},', end ="")
print()
print(count)

count = 0
for i in range(1, 3000):
    row = ""
    if i % 77 == 0:
       count += 1
       row += str(i)+ ","
    print(f'{row}', end="")

print()
print(count)
print((str(i)+ ",")[-1])

last = (2999//77)*77 #didziausias sveikas skaicius, kuris dalinasi is 77: 38*77
count = 0
for i in range(1, 3000):
    row = ""
    if i % 77 == 0:
       count += 1
       if i == last:
           print(i,end="")
       else:
            row += str(i)+ ","
            print(f'{row}', end="")

print()
print(count)


# # 3. Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
print("3.S---------------------------------------------------")
for y in range(1,26):
    row = ""
    for x in range(1,26):
        row += str(y * x) + "*"
    print(row)

# for i in range(25):
#     print("*"*25)

for y in range(1,26):
    row = ""
    for x in range(1,26):
        row += str(y * x) + "*"
    print(row)
print("---------------------------------------------------")
for y in range(1,26):
    row = " "
    for x in range(1,26):
        row += "*" + " "
    print(row)

print("---------------------------------------------------")
for y in range(25):
    row = " "
    for x in range(25):
        row += "*" + " "
    print(row)

print("---------------------------------------------------")

for y in range(1,3):
    for x in range(1,3):
        print(f'{y * x:>3}', end=" ")
    print()

print("---------------------------------------------------")
for y in range(1,4):
    row = ""
    for x in range(1,4):
        row += str(y * x) + " "
    print(row)
gal = re.sub( "[ ]", "", row)
print(gal)

for y in range(1,3):
    row = ""
    for x in range(1,3):
        row += (str(y * x))+ "*"
    print(row)
gal = re.sub( "[str(y * x)]", "nusisausiu", row)
print(gal)


# 4. Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:

# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
print("4.S---------------------------------------------------")
print("4.S.a)---------------------------------------------------")
# Iškritus herbui;
count = 0
for i in range(10):
        metimas = random.randint(0,1)
        count += 1
        print( metimas)
        if metimas == 0:
            print("H")
            break
        else:
            print("S")

print(f'meciau {count} kartu moneta, kol iskrito H')

# Tris kartus iškritus herbui;
print("4.S.b)---------------------------------------------------")

count_herbas = 0
metimu_skaicius = 0  # metimu skaicius

while count_herbas < 3:
        metimas = random.randint(0,1)
        if metimas == 0:
            print("H")
            count_herbas += 1
        else:
            print("S")

print(f'Meciau {count_herbas} kartus moneta, kol iskrito tris kartus H')

print("4.S.c)---------------------------------------------------")
# Tris kartus iš eilės iškritus herbui;
