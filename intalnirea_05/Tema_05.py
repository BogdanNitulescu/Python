'''
#Ex1

#1. Functie care sa calculeze si sa returneze suma a 2 numere

def sum2(nr1,nr2):
    return nr1+nr2

rez = sum2(4,5)
print(rez)


#Ex2
#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par(nr):
    if nr % 2 == 0:
        return True
    else:
        return False
numar= par(5)
print(numar)


#Ex3
#3. Functie care returneaza numarul total de caractere din numele tau complet.

def numar_complet(*args):
    a = 0
    for elem in args:
        a += len(elem)
    return a
rez = numar_complet('bogdan','mihai','nitulescu')
print(rez)



#ex4
#4. Functie care returneaza aria dreptunghiului

def aria_dreptunghiului(lungime,latime):
    aria = lungime * latime
    return aria
rasp = aria_dreptunghiului(10,5)
print(rasp)



import math
#Ex5
#5. Functie care returneaza aria cercului

def aria_cercului(raza):
    aria2= math.pi * raza
    return aria2
rez = aria_cercului(20)
print(rez)





#Ex6
#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu


def str(*args):
    for elem in args:
        caracter = input("introdu un caracter :")
        if caracter in elem:
            return True
        else:
            return False
string = str('Bogdan')
print(string)




#Ex7
#7. Functie fara return, primeste un string si printeaza pe ecran:

def upper_lower(nume):
    mic = 0
    mare = 0
    for elem in nume:
        if elem.islower():
            mic += 1
        if elem.isupper():
            mare += 1

    print(f'Nr de caractere lower case este {mic}')
    print(f'Nr de caractere upper case exte {mare} ')
upper_lower('BogdanMihai')




#Ex8
#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def numere_pozitive(numere):
    pozitive = []
    negative = []
    for elem in numere:
        if elem > 1:
            pozitive.append(elem)
    return pozitive
rez = numere_pozitive([-1,2,-3,2,3,4,5,6,-9])
print(rez)





#Ex9
#Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.

def numere(x,y):
    if x > y:
        print(f'{x} mai mare ca {y}')
    elif y > x:
        print(f'{y} mai mare ca {x}')
    else:
        print(f'Numerele sunt egale')
numere(7,7)




#EX10. Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def set_de_numere(set):
    numar_nou= int(input('Introdu un numar nou:'))
    nr = {}
    if numar_nou not in set:
        nr = numar_nou+1
        return f"Am adaugan un nr nou! {True}"
    else:
        return f"Numarul deja se afla in set! {False}"

rez = set_de_numere({2,3,4,5,6,1,})
print(rez)




#Ex11. Functie care primeste o luna din an si returneaza cate zile are acea luna

def zile_luna(luna):
    if luna == 1 or luna == 3 or luna == 5 or luna == 8 or luna == 10 or luna == 12:
        return f"Luna a {luna} are 31 de zile"
    elif luna == 2 :
        return f"Luna {luna} are 28 de zile!"
    else:
        return f"Luna {luna} are 30 de zile "
rez = zile_luna(2)
print(rez)



def zile_luna2(luna):
    import calendar
    rasp = calendar.monthrange(2022,luna)
    return rasp
answer = zile_luna2(5)
print(f" Luna selectata are {answer[1]} de zile")


#Ex12
#12. Functie calculator care sa returneze 4 valori
#Suma, diferenta, inmultirea, impartirea a 2 numere

#In final vei putea face:
#a, b, c, d = calculator(10, 2)
#print("Suma: ", a)
#print("Diferenta: ", b)
#print("Inmultirea: ", c)
#print("Impartirea: ", d)

def calculatro(nr1, nr2):
    suma = nr1 + nr2
    Diferenta = nr1 - nr2
    inmultirea = nr1 * nr2
    impartirea = nr1 / nr2
    return suma,Diferenta,inmultirea,impartirea



a,b,c,d = calculatro(int(input('Introduceti un nr1:')),int(input('Introduceti un nr2:')))
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)




#Ex13
#13. Functie care primeste o lista de cifre (adica doar 0-9)
#Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
#Returneaza un DICT care ne spune de cate ori apare fiecare litera

def list(lst):
    my_dict = {0: 0,1 :0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0}
    for i in range(len(lst)):
        my_dict[lst[i]] = lst.count(lst[i])
    return my_dict

r = list([9, 7, 4, 3, 0, 2, 5 ,5,1,1,1,2,])
print(r)





#EX14. Functie care primeste 3 numere
#Returneaza valoarea maxima dintre ele


def valoare_maxima(x,y,z):
    if x > y and x > z:
        return f"{x} valuare maxima"
    elif y > x and y > z:
        return f"{y} valuare maxima"
    else:
        return f"{z} valure maxima"
rez = valoare_maxima(int(input("X = ")),int(input("Y = ")),int(input("Z = ")))
print(rez)




#Ex15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
#Ex: daca dam nr 3
#Suma va fi 6 (0+1+2+3)

def suma(nr):
    suma_numerelor = 0
    for elem in range(nr+1):
        suma_numerelor = suma_numerelor + elem
    return suma_numerelor

rasp = suma(4)
print(rasp)


#16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
#‘Numele este de baiat’ sau ‘Numele este de fata’

def nume_fete(nume):
    if nume[-1] == 'a':
        return f"Numele {nume} este de fata!"
    else:
        return f"Numele {nume} nu este nume romanesc de fata! "

rasp = nume_fete(input('Introdu un nume romanesc de fata! '))
print(rasp)





#Ex17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
#Returnati numerele comune


def liste_comune(list1,list2):
    list3 = set(list1) & set(list2)
    return list3

rasp = liste_comune([1, 1, 2, 3],[2, 2, 3, 4])
print(rasp)



#EX18. Functie care sa aplice o reducere de pret
#Daca produsul costa 100 lei si aplicam reducere de 10%
#Pretul va fi 90
#Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida


def reducere(pret):
    c = int(input('Discount:')) / 100 * pret
    noul_pret = pret - c
    if c > pret:
        return 'reducerea e invalida'
    else:
        return noul_pret

rez = reducere(200)
print(rez)




#Ex19 19. Functie care sa afiseze data si ora curenta

def data_ore():
    import datetime
    acum = datetime.datetime.now()
    print(acum)
data_ore()



#20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

def zile_ramase():
    import datetime
    acum = datetime.datetime.now()
    craciun = datetime.datetime(2022,3,26)
    zile = craciun - acum
    print(acum)
    print(craciun)
    print(zile.days+1)
zile_ramase()




#Ex21  Scrieti o functie care verifica daca un numar natural dat ca argument este sau nu prim.
#!Un numar e prim daca se imparte exact NUMAI la 1 si la el insusi (nu are niciun alt divizor)!
#Ex: is_prime(17) => True
 #     is_prime(8) => False


def is_prime(nr):
    if nr / 2 == nr // 2:
        return False
    else:
        return True
s=is_prime(8)
print(s)


'''

#Ex22    Creati o functie care are ca parametrii 2 numere naturale  a,b cu a<b si returneaza lista formata din numerele prime din intervalul [a,b]
#Ex: list_of_primes_in_interval(3, 31) =>  [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def list_of_primes_in_interval(a,b):
    list = []
    for i in range(a,b+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list.append(i)
    print(list)
list_of_primes_in_interval(3,99)

