#       0 1 2 3  4 5 6 7  8
import random
import re
import time

nums = [3,5,9,78,5,0,7,20,9]
print(nums) # atspausdina visus skaicius masyve
print(nums[0]) # atspausdina pirma skaiciu is masyvo
print(nums[1]) # atspausdina antra skaiciu is masyvo
print(nums[7]) # atspausdina astunta skaiciu is masyvo
print(len(nums)) # atspausdina kiek skaiciu sudaro masyva

nums.append(60) # pabaigoje masyvo itraukia nurodyta skliausteliuose skaiciu
print(nums)

nums.sort() # surusiuoja skaicius masyve didejimo tvarka
print(nums)

nums.reverse() # surusiuoja skaicius masyve atvirksciai nei buvo
print(nums)

nums.remove(9)#pasalins 4ta elementa, nes jo reiksme 9, pasalins tik viena
print(nums)

nums.insert(3, 30) # i ketvirta vieta masyve itraukia 30
print(nums)

nums[3] = 9 # ketvirta skaiciu masyve pakeicia i 9 vietoj 30
print(nums)

print(nums.index(9)) # atspausdina indeksa, kuris turi pirma reiksme 9 masyve

nums[nums.index(9)] = 30 # masyve pakeicia nums.index(9) lygu 3 esanti 9 i 30
print(nums)

#             0              1            2          3
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius"]
print(vardai) # # atspausdina visus skaicius masyve
print(vardai[1]) # atspausdina antra varda is masyvo

belekas = [1, True, 'jo'] # masyve gali buti sudeta ivairios reiksmes


arr2d = [
    #0  1  2
    [2, 5, 6],# 0
    [84, 8, 3],# 1
    [7, 5, 9] # 2
]  # dvimatis masyvas
print(arr2d)
print(arr2d[1][2]) # atspausdina is antro masyvo trecia reiksme
print(arr2d[0][1]) # atspausdina is pirmo masyvo antra reiksme

#             0  1  2  3  4  5  6  7  8  9 indexai
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

####################### PIRMAS PARAMETRAS INCLUSSIVE(itrauktas, JĮ IMA, ANTRAS EXCLUSIVE( neitrauktas),JO NEIMA, IMA IKI JO #################
####################### Multidimensiniose masyvuose galioja tos pacios taiykles ######################################
# my_numbers[pradzia:pabaiga:zingsnis] zingsnis pagal nutylejima yra 1, jei nenurodziau kitaip

print(my_numbers) #atspausdins visa masyva
print(my_numbers[6]) #atspausdina 6 indeksa, kuris yra 7 skaicius, vienas elementas
print(my_numbers[0:4]) #nuo 0 iki 4 indekso arba nuo 1 iki 5to elemento
print(my_numbers[4:8]) #nuo 4 iki 8 indekso arba nuo 5 iki 9to elemento- keturis elementus
print(my_numbers[7:])#nuo 7 indekso arba nuo 8  elemento, iki masyvo pabaigos
print(my_numbers[:4])# nuo masyvo pradzios iki 4 indekso arba  5  elemento - keturis elementus
print(my_numbers[-2]) #antra pozicija nuo masyvo pabaigos
print(my_numbers[-5:]) #nuo 5tos pozicijos skaiciuojant nuo masyvo pabaigos iki pabaigos
print(my_numbers[:-5]) # nuo pradzios iki penktos nuo galo
print(my_numbers[2:-5]) #nuo 2os pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2]) #nuo 6tos nuo galo iki 2os nuo galo
print(my_numbers[-8:4]) #teoriskai veikia, bet neapsikraukit :D
print(my_numbers[:])#nuo pradzios iki galo
new_arr = my_numbers[:]# padaro kopiją
print(my_numbers[0:10:2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::3]) #kas trecias elementas
print(my_numbers[1::2]) #nuo pirmo elemento iki galo kas antras
print(my_numbers[3:7:2])
print(my_numbers[2:-2:2])
print(my_numbers[-8:8:2]) #nuo 8to nuo galo iki 8to nuo pradzios kas antras (nereiks tokiu, teoriskai imanoma)
print(my_numbers[::-1]) # visi elementai nuo galo, reverse
print(my_numbers[::-2]) #visi elementai nuo galo kas antras
print(my_numbers[5::-2]) #nuo 5 iki galo(tiksliau pradzios, nes einam atbulai ;) )
print(my_numbers[8:2:-2]) # nuo 8tos iki 2os, kas antras. 2a pozicija exclusive
print(my_numbers[-2:2:-2]) # nuo antros nuo galo iki antros pozicijos, kas antras atbulai


#             0              1            2          3        4          5
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius", "Jonas",'Viktoras']

print(vardai) # atspausdina masyva eilute
print(len(vardai)) # atspausdina kiek skaiciu sudaro masyva

for i in vardai: # atspausdina stulpeliu
    print(i)
print("--------________________________________________________________________________")

for vyriskis in vardai: # atspausdina stulpeliu
    print(vyriskis)
print("--------________________________________________________________________________")
for vyriskis in vardai:# atspausdina pirma masyvo reiksme tiek kartu, kiek masyve elementu, siuo atveju 6
    print(vardai[0])


print(range(0,4))

for i in range(0,4): # atspausdina stulpeliu nuo 0 iki 3 imtinai
    print(i)
print("--------________________________________________________________________________")

for i in range(4): # atspausdina labas keturis kartus
    print("labas")

print("--------________________________________________________________________________")

for i in range(4): # atspausdina visus indeksus ir vardus stulpeliu
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')

print("--------________________________________________________________________________")

for i in range(len(vardai)): # suskaiciuoja kiek yra elementu ir atspausdina visus indeksus ir vardus stulpeliu
    for i in range(len(vardai)):  # suskaiciuoja kiek yra elementu ir atspausdina visus indeksus ir vardus stulpeliu
        print(f'i = {i}, vardai[{i}] = {vardai[i]}')

print("--------________________________________________________________________________")

for i, vardas in enumerate(vardai): # atspausdina visus indeksus ir vardus sarasu
    print(i, vardas)

print("--------________________________________________________________________________")
names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
    ]
print(len(names)) # atspausdina kiek elementu masyve
print("--------________________________________________________________________________")

# select name from names where length(name) < 5;

for name in names: # du identacijos lygiai. atspausdina visus vardus, kuriu ilgis mazesnis nei 5
    if len(name) < 5:
        print(name)
print("--------________________________________________________________________________")

for i, name in enumerate(names): #naudojame kai reikia pasiekti elemento poziciją ir elementą
    if i % 10 == 0:
        print(i, name)


print("--------________________________________________________________________________")
arr2d = [
    [1, 4, 10], # 0
    [3, 5, 8], # 1
    [1, 2, 3], # 2
    [5, 10, 5], # 3
]
print(arr2d)

total_sum = 0
total_count = 0
for row in arr2d: # suskaiciuoja bendra skaiciu suma, bendra skaiciu kieki ir po to suranda vidurki
    print(row)
    total_sum += sum(row)
    total_count += len(row)
print(total_sum, total_count)
print(total_sum / total_count)

print("--------________________________________________________________________________")
total_sum = 0
total_count = 0
for row in arr2d:
    for cell in row:
        print(cell) #isspausdina visus skaicius stulpeliu
        total_sum += cell
        total_count += 1

print(total_sum / total_count)
print("--------________________________________________________________________________")
total_sum = 0
total_count = 0
for row in arr2d:
    for cell in row:
        if cell > 4: #suskaiciuoja bendra skaiciu suma, bendra skaiciu kieki ir po to suranda vidurki visu skaiciu, kurie didesni uz 4
            print(cell)
            total_sum += cell
            total_count += 1
print(total_sum , total_count)
print(total_sum / total_count)

print("--------________________________________________________________________________")
for i in range(10):
    if i  == 5:
        continue # jei atitinka salyga ignoruoja ir tesia toliau, tesia toliau ir atspausdina viska kas neatitinka salygos
    print(i)

print("--------________________________________________________________________________")
for i in range(10):
    if i % 2 == 0:
        continue #jei atitinka salyga ignoruoja,  tesia toliau ir atspausdina viska kas neatitinka salygos
    print(i)

print("--------________________________________________________________________________")

for i in range(10):
    if i == 5:
        break # atspausdina viska iki kol randa jog atitinka salyga
    print(i)

print("--------________________________________________________________________________")

for name in names:
    if name == "Patrick":
        print(name)
        break
    else:
        print("looking...")

print("--------________________________________________________________________________")

for name in names:
    if len(name) < 8: # viska kas atitinka salyga ignoruoja, o atspausdina visus kitus
        continue
    letter1 = name[0] * len(name)
    new_name = letter1 + name[1:]
    new_name = new_name.upper()
    print(new_name)

print("--------________________________________________________________________________")

for name in names: # suranda visus vardus, kuriu ilgis daugiau arba lygus 8 simboliams ir po to rastiems vardams pritaiko pasikeitima
    if len(name) >= 8:
        letter1 = name[0] * len(name)
        new_name = letter1 + name[1:]
        new_name = new_name.upper()
        print(new_name)

print("--------________________________________________________________________________")

count = 0
while True:  # prasuka skaiciu cikla ir iki kol skaicius pasidaro daugiau arba lygus penkies ir nutraukia.
    count+= 1
    if count >= 5:
        break
    print(count)

print("--------________________________________________________________________________")

count = 0
should_continue = True #
while should_continue:
    count += 1
    if count >= 5:
        should_continue = False
    print(count)

print("--------________________________________________________________________________")

count = 0
while count < 20: #bet cia jau veikia kaip for ciklas, tai geriau ir naudokit for
     count+= 1
     print(count)

print("--------________________________________________________________________________")

while True: # suka skaicius atsitiktinai ir kai randa 6, tai nutraukia
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        break

print("--------________________________________________________________________________")
count = 0
while True: # suka skaicius atsitiktinai ir kai randa 6, tai nutraukia
    dice = random.randint(1,6)
    print(dice)
    count += 1
    if dice == 6:
        break
print(count)

print("--------________________________________________________________________________")
start_time = time.time() # suskaiciuoja kiek kartu reikia mesti kauliuka, kad 6 iskristu 10 000 karu
count = 0
for i in range(10000):
    while True: #0,1666666666666667
        dice = random.randint(1,6)
        count +=1
        # print(dice)
        if dice == 6:
            break
print(f'meciau {count} kartu, kol iskrito 1000000 6tu. tikimybe yra {10000 / count}')
end_time = time.time()
print(f'paskaiciavimams prireikė {(end_time - start_time)  } sekundžių')


text = "labas vakaras studentai"
pts = text.split()
print(pts[2])
print(text[16])

for i in range(51)[10::2]:
    print(i)
print("----------------------------")
for y in range(1,11):
    for x in range(1,11):
        print(f'{y * x:>3}', end=" ")
    print()

print("----------------------------")
for y in range(1,11):
    row = ""
    for x in range(1,11):
        row += str(y * x) + " "
    print(row)

# print(5,5,5,5,5,5,5,end="")
# print(5,5,5,5,5,5,5,end="")
# print(5,5,5,5,5,5,5,end="")
# print()
# print("-----------uzd 8-------------")

print("--rusiavimas-------------------------")

#       0 1 2  3 4 5
arr = [ 1,4,12]
print(arr)
for i in range(len(arr)):
    for a in range(len(arr) -1):
        if arr[a] < arr[a+1]:
           temp = arr[a]
           arr[a] = arr[a+1]
           arr[a+1] = temp
        print(arr)

print("----------------------------")

arr = [8,1, 4, 12, 3, 2, 8]
print(arr)
for i in range(len(arr)): #bubble sort
    for a in range(i, len(arr)):
        if arr[a] > arr[i]:
            temp = arr[a]
            arr[a] = arr[i]
            arr[i] = temp
        print(arr)
    print()
arr.sort()
print(arr)


print("----------------------------")
x= 5
y= 5
gal = str(y*x)+ "+" + str( y*x)
print(gal)
print(len(gal))
