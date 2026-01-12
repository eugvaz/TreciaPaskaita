# num = 12
nums = [3,5,9,78,5,0,7,20]

print(nums[0])
print(nums[7])

print(len(nums))
nums.append(60) # pridejo i pabaiga
print(nums)
nums.sort()
print(nums)

nums.reverse()
print(nums)

nums.remove(9) #pasalins 4ta elementa, nes jo reiksme 9, pasalins tik viena
print(nums)

nums.insert( 2,30)
print(nums)

nums[3]= 9
print(nums)


my_nums= [3, 5, 9, 78, 5, 0, 7, 20]
print(my_nums)
print(my_nums[6])
print(my_nums)

# 1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
print("1.--------")
for i in range(10):
    print("labas")

print("1.--------")
for i in range(10):
    print( i+1,"labas")

# 2. Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

print("2.--------")
for i in range(0,10):
    print(i)

# Sukurkite masyvą iš dešimties augalų pavadinimų.
print("3.--------")
herbs = ["piene", "balanda", "asiuklis", "dilgele", "usnis", "varputis",
         "rugstyne", "saulute", "samana", "stubrazole"]
print(herbs)
print(len(herbs))

# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
print("4.1--------")
print(herbs)
herbs2= [["piene", "balanda", "asiuklis"],
         ["dilgele", "usnis", "varputis"],
         ["rugstyne", "saulute", "samana"],
         ["stubrazole"]]
print(herbs2)
print(herbs2[0][2])
print(herbs2[1][2])
print(herbs2[2][2])

print("4.2--------")
for i, herbs in enumerate(herbs):
    if i % 3 == 0:
        print(i, herbs)

# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio,
# ir baigiant pirmuoju. (atvirkščias ciklas).
print("5.1--------")
herbs3 = ["piene", "balanda", "asiuklis", "dilgele", "usnis", "varputis",
         "rugstyne", "saulute", "samana", "stumbrazole"]
print(herbs3)
print(herbs3[::-1])

print("5.2---------")
for i in herbs3:
    print((i),herbs3)

print("5.3---------")
for i in range(len(herbs3)):
    print(f'i = {i}, herbs3[{i}] = {herbs3[i]}')

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
print("6.--------")
for i in range(10,50):
    if i % 2 == 0:
        print(i)

# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.)
# (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

print("7.--------")
for i in range(10,50):
    if i % 2 == 0:
        print(i:)

# for i in range(10,50):
#     if i % 2 == 0:
#         print(i)
#         if i % 10 == 0:
#      continue
#      print(i)


for i in range(10,50):
    if i % 10 == 0:
       continue
    print(i)

# Sukurkite ciklą kuris suktųsi nuo 0 iki 20.
# Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
print("8.--------")

count = 0
for i in range(20):
    if i % 2 == 0:
        count = count + 1
        print(count)
    else:
        print(f"{i}")

