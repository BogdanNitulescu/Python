#Ex01
# Conditia IF cand este adevarata este executata  si cand nu este adevarata trece la urmatoarea ,
# Iar conditia ELSE daca nu a gasit mai sus nici o conditie adevarata , se va executa ca o EROARE
'''
#Ex02
x = int(input('Introduceti un nr: '))
if x > 0:
    print('Numarul tau este Pozitiv')
else:
    print('Numarul tau este negativ')


#Ex3

x = int(input('Introduceti un nr: '))
if x == 0:
    print('Numarul tau este 0')
elif x > 0:
    print('Numarul tau este pozitiv')
else:
    print('Numarul tau este negativ')



#Ex4
x = int(input('Introduceti un nr: '))
if x > -2 and x < 13 :
    print('Numarul tastat se afla intre aceste 2 numere')
else:
    print('Numarul tastat nu se afla intre aceste doua carctere!')

#Ex5
x = int(input('Introduceti un nr x: '))
y = int(input('Introduceti un nr y: '))

if x-y>5:
    print(f'diferenta {x} - {y} este mai mare decat 5')
elif x-y==5:
    print(f'diferenta {x} - {y} este 5')
else:
    print(f'diferenta {x} - {y} este mai mica decat 5')



#Ex6

x = int(input('Introduceti un nr x: '))
if x not in range(5,27):
    print('Numarul nu se afla intre aceste 2 valori!')
else:
    print('Numarul se afla intre aceste doua valori')

#Ex7
x = int(input('Introduceti un nr x: '))
y = int(input('Introduceti un nr y: '))
if x == y:
    print('Sunt Egale')
elif x > y:
    print(f"{x} Este mai mare ")
else:
    print(f"{y} este mai mare.")


#Ex8

x = int(input(' x: '))
y = int(input(' y: '))
z = int(input(' z: '))

if x == y == z:
    print('Echilateral')
elif x == y or x == z and x != y or y == z:
    print('Isoscel')
else:
    print('Oarecare')


#Ex9

litera = input('Introduceti o litera: ')
vocala = 'a','e','i','o','u'

if litera in vocala:
    print('Sunt vocale')
else:
    print('Ati introdus o consoana')



#Ex10
nota = float(input('Introduceti o Nota: '))
if nota>=0 and nota<=10 :
    if nota >= 9:
        nota='A'
    elif nota >= 8:
        nota='B'
    elif nota >=7:
        nota='C'
    elif nota >=6:
        nota='D'
    elif nota >=5:
        nota='E'
    else:
        nota='F'
    print(f"nota primita este {nota}")
else:
    print(f"nu a fost introdusa o nota valida")



#Ex11

x = int(input(' x: '))
x= str(x)

if len(x) >= 4:
    print(f'{x} Are mai mult de 4 cifre! ')
else:
    print(f'{x} Nu este compus din 4 cifre! ')



#Ex12
x = int(input(' x: '))
x= str(x)

if len(x) == 6:
    print(f'{x} Are exact 6 cifre! ')
else:
    print(f'{x} Nu are 6 cifre ! ')


#Ex13
x = int(input(' x: '))
if x % 2 == 0:
    print(f'{x} Este par')

else:
    print(f'{x} Este impar')


#Ex14
x = int(input(' x: '))
y = int(input(' y: '))
z = int(input(' z: '))

if x > y  and x > z:
    print(f'{x} Este mai mare ')
elif x < y and y > z:
    print(f'{y} Este mai mare ')
else:
    print(f'{z} Este mai mare')


#Ex15

x = int(input(' x: '))
y = int(input(' y: '))
z = int(input(' z: '))
g = x + y + z
if g == 180:
    print(' triunghiul este complet ')
else:
    print(' datele nu sunt corecte')



#Ex16
# Given the string "fox, cat, cow, horse". Display the following message "You found your dog" if 'dog' is in the string,
# otherwise print the last animal from the string

animals="fox, cat, cow, horse"
if animals.find("dog")>=0:
    print('Ti-am gasit catelul!')
else:
    x = animals.split(', ')
    print(x[-1])


#Ex Titi
x = int(input('x='))
if x == 0:
    print(f'{x} Este egal cu 0')
elif x > 0:
    print(f'{x} Este Pozitiv')
else:
    print(f'{x} Este negativ')


#Ex Bog
x = int(input(' x: '))
y = int(input(' y: '))
z = int(input(' z: '))
volum = x * y * z
print(volum)


#Se citesc 3 numere întregi. Câte sunt pare?

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))


if x % 2 ==0 and y % 2 ==0 and z % 2 ==0:
    print('Avem 3 numere pare')

elif x % 2 ==0 and y % 2 ==0 or z % 2 ==0 and y % 2 ==0 or x % 2 ==0 and  z % 2 ==0:
    print('Avem 2 numere pare')
elif x % 2 ==0 or y % 2 ==0 or z % 2 ==0 :
    print('Avem 1 numere pare')


else:
    print('Nu avem numar par')



x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
g = 0
if  x % 2 ==0 and g = g+1 or  y % 2 ==0 and g = g+1 or  z % 2 ==0 and g = g+1:


print(f'Avem {g} nr pare! ')



#Ziua 2 Tema 2 refacuta

#Ex2

x = int(input('X = '))
if x > 0:
    print(f'{x} Este numar pozitiv')
else:
    print(f'{x}Este numar negativ')

#Ex3
x = int(input('X = '))
if x > 0:
    print(f'{x} Este numar pozitiv')
elif x == 0:
    print(f'{x} Este numar neutru')
else:
    print(f'{x} Este numar negativ')



#Ex4
x = int(input('X = '))
if x > -2 and x < 13:
    print(f'{x} Se afla intre aceste 2 numere ')
else:
    print(f'{x} Nu se afla intre aceste numere')


#Ex5
x = int(input('X = '))
y = int(input('y = '))

if x - y > 5 or y - x > 5:
    print('Diferenta este mai mare de 5')
elif x - y == 5:
    print('Diferenta este 5')
else:
    print('Diferenta este mai mica decat 5')





#Ex6

x = int(input('X = '))
if x not in range(5,27):
    print(f'{x} nu se afla intre 5 si 27')
else:
    print(f'{x} Se afla intre 5 si 27')



#Ex7

x = int(input('X = '))
y = int(input('y = '))

if x > y:
    print(f'{x} este mai mare')
elif y > x:
    print(f'{y} este mai mare ')
else:
    print('Numerele sunt egale')



#Ex8
x = int(input('X = '))
y = int(input('y = '))
z = int(input('z = '))

if x == y and y == z:
    print('Echilateral')
elif x == y or x == z and y != z or y == z:
    print('Isoscel')
else:
    print('Oarecare')



#Ex9
x = str(input('Tasteaza o litera: '))
vocale = 'a','e','i','o','u'

if x not in vocale:
    print(f'{x} Este o Consoana')
else:
    print(f'{x} Este o Vocala')



#Ex10

nota = int(input('Nota este : '))

if nota >= 9:
    print("A")
elif nota >= 8:
    print("B")
elif nota >= 7:
    print("C")
elif nota >= 6:
    print("D")
elif nota >= 4:
    print("E")
else:
    print('F')


#Ex11
x = input('Introduceti un numar: ')
l = len(x)
if l >= 4:
    print(f'{x} este compus din {l} cifre')
else:
    print(f'{x} este sub 4 cifre , si este compus din {l} cifre')



#Ex12
x = input('Introduceti un sir de numere : ')
l = len(x)

if l == 6:
    print(f'{x} are exact 6 cifre')
else:
    print(f'{x} nu are are exact 6 cifre , are {l} cifre. ')



#EX13
x = int(input("x = "))
if x % 2 == 0:
    print('Avem un nr par')
else:
    print('Avem un nr impar')


#Ex14

x = int(input('X = '))
y = int(input('y = '))
z = int(input('z = '))

if x > y and x > z:
    print(f'{x} Este cel mai mare ')
elif y > x and y > z:
    print(f'{y} Este cel mai mare ')
else:
    print(f'{z} Este mai mare')


#Ex15

x = int(input('X = '))
y = int(input('y = '))
z = int(input('z = '))
v = x+y+z

if v == 180:
    print(f'Suma tuturor laturilor este {v} de grade si triunghiul este valid ')
else:
    print(f'Suma tuturor laturilor este {v} de grade si nu este un triunghi valid ')


'''

#Ex16
age = int(input('introduceti varsta: '))
pasaport = input('Are pasaportul valid : DA/NU ')
ambii_parinti = input('Are ambii parinti? DA/NU ')
permisiune = input('Are permisiune? DA/NU/NA ')

if age >=18 and pasaport == 'DA':
	print('permite calatoria')
elif pasaport == 'DA' and ambii_parinti == 'DA' or permisiune == 'DA' :
    print('Permite calatoria')
else :
    print('Nu permite calatoria')


