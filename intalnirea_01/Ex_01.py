#Ex1
# O variabila este o locatie ce ii putem da noi valori si nume
'''
#Ex2
Nume = 'Bogdan'
Varsta = 27
Inaltime = 1.75
Sex_masculin = True

print(Nume)
print(Varsta)
print(Inaltime)
print(Sex_masculin)

#Ex3
print(type(Nume))
print(type(Varsta))
print(type(Inaltime))
print(type(Sex_masculin))

#Ex4
round(Inaltime)
print(round(Inaltime))
print(type(Inaltime))

#Ex5
print('Numele meu este ' +Nume)
print(f'Si am  {Varsta}')
print(f'Am inaltimea de {Inaltime}')
print(f'Si sunt de sex masculin :{Sex_masculin}')

#Ex6
Nume = input('Numele dumneavoastra este :' )
Prenume = input('Prenumele Dumneavoastra este: ')
nume_complet = Nume + Prenume

print((len(nume_complet)))

#Ex7
Lungime = input('Lungimea')
latime = input('Latime')
aria = int(Lungime) * int(latime)

print(aria)


#Ex8
P = 'Corla is either the stupidest animal or the smartest rock'
C = input('Introduceti un nr: ')

print(P[:-int(C)])


#Ex9
P = 'Corla is either the stupidest animal or the smartest rock'
print(P[5:-5])


#Ex10
P = 'Corla is either the stupidest animal or the smartest rock'
print(P.count('the'))

#Ex11
P = 'Corla is either the stupidest animal or the smartest rock'
print(P.replace('the','THE'))

#Ex12
P = 'Corla is either the stupidest animal or the smartest rock'
print(P.find('rock'))
print(P[0:53])

#Ex13
Nume = 'Bogdan'
Varsta = 27
Inaltime = 1.75
Sex_masculin = True
var = Nume + str(Varsta) + str(Inaltime) + str(Sex_masculin)
print(f'Numele meu este {Nume} am varsta de {Varsta}, o inaltime de  {Inaltime} ,si o urasc pe Titi : {Sex_masculin}')



#Ex14
Nr = '0123456789'
print(Nr[::2])
print(Nr[1::2])


#Ex15
L = input('Introduceti Lungimea')
l = input('Introduceti Latime')
Aria = int(L) * int(l)

print(Aria)



#Ex16
S = input('Tastati un text impar:')
print(len(S))
print(S[len(S)//2])


#Ex17
A, B = input('Tastati doua cuvintele: ') .split(' ')


print(A)
print(B)


#Ex18
b = input('Tastati: ')
var = b[0]]+
c = b[0b[1:-1].replace(var,var.upper()) + b[-1]
print(c)

'''



"""
#Ex19
user = input('introduceti un nume de utilizator: ')
parola = input('introduceti parola: ')
l = (len(parola))
nr = l * '*'
print(f'Parola pt user este {nr} si are {l} caractere')





P = 'Corla is either the stupidest animal or the smartest rock'
print(P.count('the'))

"""

'''Printati cei 3 elevi si notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o veti lua folosindu-va de cheie'''
'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

#practic vreau sa afisezi '{var_pt_cheie} a luat nota {var_pt_valoare}' folosindu`te de for si construindu`ti tu variabilele astea 2)

'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
var_key = dict1['Ana']


for nota, stock_count in dict1.items():
    print('A luat nota ' + str(stock_count) + ' ' + nota + ' ! ')