#Ex4
'''
#V1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini = range(9)


for a in masini:
    print(f"Masina mea preferata este {a}")


for masini in range(9):
    print(masini)

#V2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(1,len(masini)-1):
    masini[i]=masini[i].upper()
else:
    print(masini)




#Ex3

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina Dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masina}, mai cautam .')




#Ex4

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for lux in masini:
    if lux == "Lastun" or lux == "Trabant":
        continue
    print(f'Sar puttea sa va placa  masina {lux}')





#Ex5

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        masini_vechi.append(masina)
        masini[5] = 'TeslaX'
print(f'Masinile vechi sunt {masini_vechi}')
masini[7] = 'Tesla'
print(f'Masinile noi sunt {masini}')



#Ex6
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for key,value in pret_masini.items():
    if value <= 15000:
        print(F'Masinile disponibile sunt {key},{value}')


#Ex7
#Avand lista
#Iterati prin ea
#Afisati de cate ori apare 3
#(nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
n = 0
for n in numere:
    if  n == 3:
        n = n+1
print(n)


#ex8

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for numar in numere:
    sum =sum + numar
print(f'Suma totala este {sum}')



#Ex9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

def numeremari(numere):

    nr = numere[0]

    for num in numere:
        if num > nr:
            nr = num
    return  nr
print(numeremari(numere))



#Ex10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr = []
for n in numere:
    if  n > 0:
        n = -n
        nr.append(n)

print(nr)



#11.
#Iterati prin lista alte_numere
#Populati corect celelalte liste
#Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for n in alte_numere:
    if n % 2 == 0 :
        numere_pare.append(n)
    if n % 2 != 0 :
        numere_impare.append(n)
    if n > 0 :
        numere_pozitive.append(n)
    if n < 0 :
        numere_negative.append(n)
print(f' Numere pare {numere_pare}')
print(f'Numere impare {numere_impare}')
print(f'Numere pozitive {numere_pozitive}')
print(f'Numere negative {numere_negative}')

for n in range(0,len(alte_numere)):
    for j in range(n+1,len(alte_numere)):
        if (alte_numere[n] > alte_numere[j]):
            alte_numere[n],alte_numere[j] = alte_numere[j],alte_numere[n]
print(alte_numere)





#Ex12
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for n in range(0,len(alte_numere)):
    for j in range(n+1,len(alte_numere)):
        if (alte_numere[n] > alte_numere[j]):
            alte_numere[n],alte_numere[j] = alte_numere[j],alte_numere[n]
print(alte_numere)



#Ex13


import random
numar_secret=random.randrange(1,30)
nr_inceput=1
nr_final=30
while True:
     numar=input(f'Ghiceste un numar intre {nr_inceput} si {nr_final}:')
     try:
         numar=int(numar)
     except:
         print("Nu ati introdus un nr")
     else:
         if numar== numar_secret:
             print('Felicitari,ai ghicit')
             break
         elif numar<numar_secret:
             print('Nr secret e mai mare')
             nr_inceput=numar
         else:
             print('Nr secret e mai mic')
             nr_final=numar



#ex14
nr = int(input('Introduceti un nr:'))
else:
    for i in range(nr + 1):
        print(i * str(i))


print('\tEX_15')
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for i in range(len(tastatura_telefon)):
    lista_curenta=tastatura_telefon[i].copy()
    for j in range(len(tastatura_telefon[i])):
        print(f'elementul curent este {lista_curenta[j]}')
'''

