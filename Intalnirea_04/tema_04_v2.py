#Ex1
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#V1
for element in masini:
    print(f"Masina mea preferata este : {element}")
#V2
for b in range(len(masini)):
    print(f'Masina mea preferata este :: {masini[b]}')
#V3
m = len(masini)
n = 0
while m > 0:
    print(f"Masina mea preferata este :::{masini[n]}")
    n += 1
    m -= 1

#Ex2

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for element in range(1,len(masini) - 1 ):
        masini[element] = masini[element].upper()
else:
    print(masini)


#Ex3

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for  cumparator in masini:
    if cumparator == 'Mercedes':
        print(f'Am gasit masina dorita de dvs! {cumparator}')
        break
    else:
        print(f'Am gasit masina {cumparator}.Mai cautam')




#Ex4
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for cumparator in masini:
    if cumparator == 'Trabant' or cumparator == 'Lasunt ':
        continue
    print(f"Sar putea sa va placa masina: {cumparator} !")


#Ex5

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for elem in masini:
     if elem == 'Trabant' or elem == 'Lastun':
         masini_vechi.append(elem)
         masini[masini.index(elem)]='Tesla'

print(masini)
print(masini_vechi)




#Ex6

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

pret = input('Adaugati un buget : ')

#V1
try:
    pret = int(pret)
except:
    print('Nu ati introdus o suma valida! ')
else:
    for elem in pret_masini.items():
        if int(elem[1]) < pret:
            print(f'Pentru bugetul dumneavoastra de {pret}, avem masina {elem[0]}')



#V2
try:
    pret = int(pret)
except:
    print('Nu ati introdus o suma valida! ')
else:
    for elem in pret_masini:
        if pret_masini[elem] < pret:
            print(f"Pentru bugetul dumneavoastra de {pret}, avem doar masina {elem}. ")




#Ex7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
c = 0
for elem in numere:
    if elem == 3 :
        c += 1
print(f'Numarul 3 apare de {c} ori.')




#Ex8

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

s = 0

for elem in numere:
    if elem in numere:
        s += elem
print(f'Suma numerelor este {s}')



#Ex9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

nr = numere[0]

for elem in numere:
    if elem > nr:
        nr = elem
print(f"Nr. cel mai mare este {nr}")



#Ex10

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for elem in numere:
    if elem > 0:
        numere[numere.index(elem)] =- elem
print(numere)



#Ex11
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for elem in alte_numere:
    if elem % 2 == 0:
        numere_pare.append(elem)
    else:
        numere_impare.append(elem)
    if elem > 0:
        numere_pozitive.append(elem)
    if elem < 0:
        numere_negative.append(elem)
print(f'Numerele impare sunt : {numere_impare}')
print(f'Numerele negative sunt : {numere_negative}')
print(f'Numerele pozitive sunt : {numere_pozitive}')
print(f'Numerele pare sunt : {numere_pare}')



#Ex12

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
h = sorted(alte_numere,reverse=True)

print(h)





#Ex13

#numar_secret = Generati un numar random intre 1 si 30
#Numar_ghicit = None

import random
numar_secret = random.randint(1,30)
i = 1
s = 30
while True:
    try:
        numar = int(input(f'Introduceti un nr intre {i} si {s}:'))
    except:
        print('Nu ati introdus un Numar! ')
    else:
        if numar == numar_secret:
            print('Ati ghicit')
            break
        elif numar < numar_secret:
            print("Numarul este mai mare!")
            i = numar
        else:
            print('Numarul este mai mic!')
            s = numar




#Ex14

try:
    a = int(input('Introduceti un nr. : '))
except:
    print('Nu ati introdus un nr. valid!')
else:
    for nr in range(a+1):
        print(nr * str(nr))

'''