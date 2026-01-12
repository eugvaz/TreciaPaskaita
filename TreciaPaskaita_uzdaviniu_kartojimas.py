import random

# 1. Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
print("1.---------------------------------------------------")
for i in range(10):
    print("labas")

for i in range(10):
    print(i,"labas")

# 2. Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
print("2.---------------------------------------------------")

for i in range(0,10):
    print(i)

# 3. Sukurkite masyvą iš dešimties augalų pavadinimų.
print("3.---------------------------------------------------")
# 10 nuodingu augalu
herbs = ["briene","difenbachija","drugisius","durnarope","isne","kurpele", "mandragora", "pipirlape", "pupmedis", "ugniazole"]
print(len(herbs))

for herb in herbs:
    print(herb)

# 4. Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
print("4.---------------------------------------------------")
print(len(herbs))
for herb in herbs:
    print(herb)
print("-------------------------")
for i in range(len(herbs)):
    print(f'i = {i}, augalai[{i}] = {herbs[i]}')
print("-------------------------")
for i, herb in enumerate(herbs):
    print(i,herb)
print("-------------------------")
for i in range(len(herbs)):
    print(i,herbs[i])
print("-------------------------")
for i, herb in enumerate(herbs, start=1):
    print(i,herb)


# 5. Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
print(herbs[::-1])
print("5.---------------------------------------------------")
for herb in herbs[::-1]:
    print(herb)

for i, herb in enumerate(herbs[::-1], start=1): # tikrinti elementus nuo pabaigos i pradzia ir juos sunumeruoti pradedant nuo 1
    print(i,herb)

# 6. Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
print("6.---------------------------------------------------")
count = 0
for i in range(10,51):
    if i % 2 == 0:
        print(i)
        count +=1
print(count)
print("-------------------------")
count = 0
for i in range(10,51,2):
     print(i)
     count += 1
print(count)
# print("-------------------------")
# count = 0
# for i in range(51)[10::2]:
#     print(i)
#     count += 1
# print(count)

# 7. Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.)
# (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
print("7.---------------------------------------------------")
count = 0
for i in range(10,51,2): # pradedame nuo 10 ir iki 50,zingsnis kas antras arba pridedama po 2
    if i % 10 == 0:
        continue #ignoruojame viska kas dalinasi is 10
    print(i)
    count += 1
print(count)


# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
print("8.---------------------------------------------------")
count = 0
for i in range(0,21): # pradedame nuo 0 ir iki 20,zingsnis kas vienas arba pridedama po 1
    if i % 2 == 0:
        print(i)
        count += 1
print("kiek cikle poriniu reiksmiu:",count)

# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai.
# (du skaičiavimai)
print("9.---------------------------------------------------")
# 10 nuodingu augalu
herbs = ["briene","difenbachija","drugisius","durnarope","isne","kurpele", "mandragora", "pipirlape", "pupmedis", "ugniazole"]
print(len(herbs))

count = 0
for herb in herbs:
    if len(herb) < 5 or len(herb) > 7:
        print(herb)
        count += 1
    else:
        print(f'neatitinka salygos')
print("kiek cikle tokiu augalu:",count)

print("-------------------------")
count = 0
for herb in herbs:
    if len(herb) < 5 or len(herb) > 7:
        print(herb)
        count += 1
print("kiek cikle tokiu augalu:",count)

print("-------------------------")

count = 0
for herb in herbs:
    if 5 <= len(herb) <= 7:
        continue
    else:
        print(herb)
        count += 1
print("kiek cikle tokiu augalu:",count)

print("-------------------------") # su masyvu
herbs = ["briene","difenbachija","drugisius","durnarope","isne","kurpele", "mandragora", "pipirlape", "pupmedis", "ugniazole"]
print(len(herbs))

atitinkantys_salyga = [] #sukuriamas tuscias masyvas
for herb in herbs:
    if len(herb) < 5 or len(herb) > 7:
        atitinkantys_salyga.append(herb)
print("Atitinkantys salyga augalu pavadinimai:", atitinkantys_salyga)
print(len(atitinkantys_salyga))

# 10. Suskaičiuokite kiek 3čio uždavinio masyve yra
# žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
print("10.---------------------------------------------------")
count = 0
for herb in herbs:
    if 5 < len(herb) < 10:
        print(herb)
        count += 1
print("kiek cikle tokiu augalu:",count)
print("-------------------------")
count = 0
for herb in herbs:
    if 5 < len(herb) < 10:
        print(herb)
        count += 1
    else:
        print(f'neatitinka salygos')
print("kiek cikle tokiu augalu:",count)

# 11. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais vienoje eilutėje
# ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
print("11.---------------------------------------------------")
sk = 0 # sukurimas skaitiklis
for i in range(300): # cikle sukasi 300 atsitiktiniu skaiciu
    dice = random.randint(0,300)
    if dice > 150:
        sk += 1
    if dice > 275:
        print(f'[{dice}]', end=" ")
    else:
        print(dice, end=" ")
print()
print(sk)

# 12.Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.
print("12.---------------------------------------------------")

sk = 0 # sukurimas skaitiklis
for i in range(1,3001):
    if i % 77 ==0:
        print( f'{i},', end ="")
        sk += 1
print()
print(sk)
print("-------------------------")

sk = 0
last = (3000//77)*77 # paskutinis esantis siame cikle, kad butu aisku po ko nedeti kablelio
for i in range(1, 3000):
    row = ""
    if i % 77 == 0:
       sk += 1
       if i == last:
           print(i, end="")
       else:
           row += str(i) + ","
           print(f'{row}', end="")

print()
print(sk)

print("-------------------------")
sk = 0
last = (3000//77)*77 # paskutinis esantis siame cikle, kad butu aisku po ko nedeti kablelio
for i in range(1, 3000):
    if i % 77 == 0:
        if i == last:
            print(i, end="")
        else:
            print(i, end=",")
print()
print(sk)

# 13. Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# * * * * * * * * * * *
print("13.---------------------------------------------------")
for y in range(25): # isorinis ciklas, kuris atspausdina 25 eilutes
    row = "" # string su tusciu tekstu kur bus sudeta vienos eilutes informacija( kiek simboliu eiluteje)
    for x in range(25): # vidinis ciklas sukasi 25 kartus bus atspausdinta zvaigzdute su tarpu eiluteje
        row += "*" + " "
        #row = row +"* "
    print(row)
print("-------------------------")
for _ in range(25): #atspausdina 25 eilutes, _ reiskia, kad man sis kintamasis nereikalingas
    print("* "*25) #eiluteje yra 25 * su tarpais


# 14.Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
print("14.---------------------------------------------------")

# for _ in range(25): #atspausdina 25 eilutes, _ reiskia, kad man sis kintamasis nereikalingas
#     print("* "*25) #eiluteje yra 25 * su tarpais


# 15. Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
print("15.---------------------------------------------------")
print("-------------------------")
# Iškritus herbui;
sk = 0 #skaiciuoju metimus
for i in range(100): # pataisyti i while true
    metimas= random.randint(0,1)
    sk += 1
    if metimas == 0:
        print("H")
        break
    else:
        print("S")
print("kelintu metimu iskrito herbas:",sk)
print("a-------------------------")
# for i in range(100): pakeista i while True:
print("spresta_per_paskaita-------------------------")
while True:
    metimas = random.randint(0,1)
    if metimas == 0:
        print("H")
        break
    else:
        print("S")

print("----------------------------------------")

# Tris kartus iškritus herbui;
sk_herbu = 0
sk_metimu = 0
for i in range(100): # apribota metimu imtis # pataisyti i while true
    metimas= random.randint(0,1)
    sk_metimu +=1
    if metimas == 0:
        print("H")
        sk_herbu +=1
        if sk_herbu >= 3:
            break
    else:
        print("S")
print()
print("Per kiek metimu iskrito 3 herbai:", sk_metimu)
print("b-------------------------")
# Tris kartus iškritus herbui;
sk_herbu = 0
sk_metimu = 0
while sk_herbu < 3: # mes tol kol iskris trys herbai
    metimas= random.randint(0,1)
    sk_metimu +=1
    if metimas == 0:
        print("H")
        sk_herbu +=1
        if sk_herbu == 3:
            break
    else:
        print("S")
print("Per kiek metimu iskrito 3 herbai:", sk_metimu)
print("spresta_per_paskaita-------------------------")
print("----------------------------------------")
# Tris kartus iškritus herbui; A
sk_herbu = 0
while True:  # sustabdome metyma, kai herbas iskrenta tris kartus
    metimas = random.randint(0,1)
    if metimas == 0:
        print("H")
        sk_herbu += 1
        if sk_herbu >= 3:
            break
    else:
        print("S")
print("----------------------------------------")

# Tris kartus iškritus herbui; B
sk_herbu = 0
while True:
    metimas = random.randint(0, 1)
    if metimas == 0:
        print("H")
        sk_herbu += 1
    else:
        print("S")
    if sk_herbu >= 3:
        break
print("----------------------------------------")

# Tris kartus iškritus herbui; C
sk_herbu = 0
while sk_herbu < 3:
    metimas = random.randint(0, 1)
    if metimas == 0:
        print("H")
        sk_herbu += 1
    else:
        print("S")
print("----------------------------------------")


print("-------------------------")
# Tris kartus iš eilės iškritus herbui;

sk_herbu_is_eile = 0
sk_metimu = 0
while sk_herbu_is_eile  < 3: # mes tol kol iskris trys herbai is eiles
    metimas= random.randint(0,1)
    sk_metimu +=1
    if metimas == 0:
        print("H")
        sk_herbu_is_eile += 1
        # if sk_herbu_is_eile == 3:
        #     break
    else:
        print("S")
        sk_herbu_is_eile = 0
print("Per kiek metimu iskrito 3 herbai is eiles:", sk_metimu)
print("-------------------------")
sk_herbu_is_eile = 0
sk_metimu = 0
while True: # mes tol kol iskris trys herbai is eiles
    metimas= random.randint(0,1)
    sk_metimu +=1
    if metimas == 0:
        print("H")
        sk_herbu_is_eile += 1
        if sk_herbu_is_eile >= 3:
            break
    else:
        print("S")
        sk_herbu_is_eile = 0
print("Per kiek metimu iskrito 3 herbai is eiles:", sk_metimu)

print("spresta_per_paskaita-------------------------")
count = 0
count_h = 0
while True:
    coin = random.randint(0, 1)
    count += 1
    if coin == 0:
        print("H")
        count_h += 1
    else:
        print("S")
        count_h = 0
    if count_h >= 3:
        break
print(count,count_h)

# 16. Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”.
# Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas, kas greičiau surenka 222 taškus.
# Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.
print("16.---------------------------------------------------")
print("-------------------------")
Petro_taskai_viso = 0
Kazio_taskai_viso = 0
partijos = 0
while Kazio_taskai_viso < 222 and Petro_taskai_viso < 222: # sita vieta pasikoreguoti pagal while true
    Petro_taskai = random.randint(10, 20)
    #print("Petro taskai",Petro_taskai)
    Kazio_taskai = random.randint(5, 25)
    #print("Kazio taskai",Kazio_taskai)
    Petro_taskai_viso += Petro_taskai
    #print("Visi Petro taskai", Petro_taskai_viso)
    Kazio_taskai_viso += Kazio_taskai
    #print("Visi Kazio taskai", Kazio_taskai_viso)
    if Petro_taskai != Kazio_taskai:
        partijos += 1
        #print(partijos)
        if Petro_taskai > Kazio_taskai:
            print( "Partiją laimėjo:",partijos,"Petras", Petro_taskai,">", Kazio_taskai,".Bendras tasku skaicius: P =",Petro_taskai_viso,", K =", Kazio_taskai_viso)
        else:
            print("Partiją laimėjo:",partijos,"Kazys", Kazio_taskai, ">", Petro_taskai,".Bendras tasku skaicius: P =",Petro_taskai_viso,", K =", Kazio_taskai_viso)
    else:
        print("Lygu.",partijos," Abu surinko po tiek pat tasku:", "Petras",Petro_taskai,"=","Kazys", Kazio_taskai)
print()
if Petro_taskai_viso != Kazio_taskai_viso:
    if Petro_taskai_viso> Kazio_taskai_viso:
        print("Zaidima laimėjo Petras")
    else:
        print("Zaidima laimėjo Kazys")
else:
    print("Zaidimas baigesi lygiosiomis")
print()


print("spresta_per_paskaita-------------------------")
k_pts_t = 0
p_pts_t = 0
while True:
    k_pts = random.randint(5,25)
    p_pts = random.randint(10,20)
    k_pts_t += k_pts
    p_pts_t += p_pts
    if k_pts > p_pts:
        print(f'Partiją laimėjo Kazys su taškų persvara {k_pts} > {p_pts}. bendras taškų balansas P:{p_pts_t}, K:{k_pts_t}')
    elif p_pts > k_pts:
        print(f'Partiją laimėjo Petras su taškų persvara {p_pts} > {k_pts}. bendras taškų balansas P:{p_pts_t}, K:{k_pts_t}')
    else:
        print(f'Partija baigėsi lygiosiomis abiems žaidėjams surinkus po {p_pts} taškų.')
    if k_pts_t >= 222 or p_pts_t >= 222:
        break
if k_pts_t > p_pts_t:
    print("Žaidimą laimėjo Kazys")
elif p_pts_t > k_pts_t:
    print("Žaidimą laimėjo Petras")
else:
    print("Žaidimas baigėsi lygiosiomis")


# 17. Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija.
# Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė
# (pasinaudokite random.randint(x,x)funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį.
# Suskaičiuokite kiek reikia smūgių.

print("17.---------------------------------------------------")
print("-------------------------")

# Vienas_ikaltas_vinis = 85
# Ikalta_viniu_viso = 0
# Smugiu_skaicius = 0
#
# while Ikalta_viniu_viso < 5* Vienas_ikaltas_vinis:
#     Vinies_ikalimo_gylis = random.randint(5,20)
#     Ikalta_viniu_viso += Vinies_ikalimo_gylis
#     Smugiu_skaicius += 1
#     print("Vinies ikalimo gylis:",Vinies_ikalimo_gylis)
# print("Smugiu skaicius: ", Smugiu_skaicius)
# print("Viso ikalta viniu: ", Ikalta_viniu_viso)
#
# print("-------------------------")
#
Vienas_ikaltas_vinis = 85
Ikalta_viniu = 0
Smugiu_skaicius = 0


for Vinis in range(5): # ciklas sukasi 5 kartus, nes kalame 5 vinis
    Ikalta_vinis = 0
    Smugiai_siai_viniai_kalti = 0
    print("Kalama vinis:", Vinis)
    while Ikalta_vinis < Vienas_ikaltas_vinis:
          Vinies_ikalimo_gylis = random.randint(5,20)
          Ikalta_vinis += Vinies_ikalimo_gylis
          Ikalta_viniu += Vinies_ikalimo_gylis
          Smugiai_siai_viniai_kalti += 1
          Smugiu_skaicius += 1
    print(Vinis,"Ikalta vinis:",Ikalta_vinis)
    print("Smugiu skaicius: ", Smugiai_siai_viniai_kalti)
print()
print("viso smugiu skaicius",Smugiu_skaicius)
print("Ikalta viso viniu:", Ikalta_viniu)

print("-------------------------")
print("-------------------------")

Vienas_ikaltas_vinis = 85
#Ikalta_viniu = 0
Smugiu_skaicius = 0


for Vinis in range(5): # ciklas sukasi 5 kartus, nes kalame 5 vinis
    Ikalta_vinis = 0
    Smugiai_siai_viniai_kalti = 0
    print("Kalama vinis:", Vinis)
    while Ikalta_vinis < Vienas_ikaltas_vinis:
        Tikimybe_pataikyti_i_vini = random.randint(0,1)
        Smugiai_siai_viniai_kalti += 1
        Smugiu_skaicius += 1
        if Tikimybe_pataikyti_i_vini == 1 :
            print("pataike i vini")
            Vinies_ikalimo_gylis = random.randint(20,30)
            Ikalta_vinis += Vinies_ikalimo_gylis
            Ikalta_viniu += Vinies_ikalimo_gylis
            #Smugiai_siai_viniai_kalti += 1
            print(Vinis,"Ikalta vinis:",Ikalta_vinis)
            print("Smugiu skaicius: ", Smugiai_siai_viniai_kalti)
        else:
            print("nepataike i vini")
print()
print("viso smugiu skaicius",Smugiu_skaicius)
#print("Ikalta viso viniu:", Ikalta_viniu)

print("-------------------------")
print("spresta_per_paskaita-------------------------")
total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        taukst = random.randint(5,20)
        total_taukst += taukst
        count += 1
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.')
print(f'Iš viso prireikė {total_count} smūgių')


# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        count += 1
        if random.randint(0,1) == 0:
             continue
        taukst = random.randint(20,30)
        total_taukst += taukst
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.')
print(f'Iš viso prireikė {total_count} smūgių')
print("----------------------------------------")

total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        count += 1
        taukst = random.randint(20,30) * random.randint(0,1)
        total_taukst += taukst
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.') # komentaras
print(f'Iš viso prireikė {total_count} smūgių')
print('Dovilės kodas')
print()

