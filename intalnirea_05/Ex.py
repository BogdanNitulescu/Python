#ex1  1. Functie care sa calculeze si sa returneze suma a 2 numere

'''
def func(x, y):
    res = x +y
    print(f'Suma dintre {x} si {y}: {res}')


func(3, 2)

#Ex2  2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def retu(x):
    if x % 2 == 0:
        return True
    else:
        return False
rasp = retu(6)
print(rasp)

#Ex 3 3. Functie care returneaza numarul total de caractere din numele tau complet.

def nume(nume1, prenume, nume_mijlociu):
    return f'Numarul total de caractere din {nume1} {prenume} {nume_mijlociu},are {len(nume1+prenume+nume_mijlociu)}'

nr = nume('Bogdan','Mihai','Nitulescu')
print(nr)

#Ex 4 4. Functie care returneaza aria dreptunghiului

def func(x, y):
    ar = x * y
    return f'Aria dreptunghiului este {ar}'
aria = func(5,10)
print(aria)

#Ex5 5. Functie care returneaza aria cercului

def cerc(raza):
    r = math.pi * (raza ** 2)
    return f'Aria cercului este {r}'
aria = cerc(3)
print(aria)

#Ex6 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def string(str):
    caracter = input('Introduceti un caracter : ')
    if caracter in str:
        return True
    else:
        return False
ans = string('Bogdan')
print(ans)


#Ex7 7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y

def upper_lower(str1):
    case = {'upper':0, 'lower':0}
    for letter in str1:
        if letter.isupper():
            case['upper']=case['upper'] + 1
        if letter.islower():
            case['lower'] = case['lower'] + 1
    print('originals:',str1)
    print('upper:',case['upper'])
    print('lower:',case['lower'])

upper_lower('Bogdan Mihai Nitulescu')
#v2
def up_lo(str1):
    c_low = 0
    c_upp = 0
    for elem in str1:
        if elem.isupper():
            c_upp += 1
        if elem.islower():
            c_low += 1
    print(f'Caractere mici {c_low}')
    print(f'Caractere mari {c_upp}')
up_lo('Bogdan Mihai Nitulescu')





#Ex 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def pozitiv(numere):
    numere_pozitive = []
    for elem in numere:
        if elem > 0:
            numere_pozitive.append(elem)
    return sorted(numere_pozitive)



answ = pozitiv([1, -2, 6, 2, 7, -13, 17, 29])
print(answ)




#9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.

def zero(x,y):
    if x > y:
        return f"{x} este mai mare decat {y}"
    elif y > x:
        return f"{y} este mai mare decat {x}"
    else:
        return f" Numerele {x} si {y} sunt egale"
nr = zero(8,5)
print(nr)


#Ex10
#10. Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def nr_set(set):
    n = int(input("nr = "))
    nr = {}
    if n not in set:
        nr=n+1
        return f"Am adaugat nr nou {True}"
    else:
        return f"nu am adaugat numarul in set. Acesta exista deja {False}"

nr1 = nr_set({1,2,3,4})
print(nr1)



#Ex11 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

def calendar(string):
    for luna in string:
        if luna == '1' or luna == '3' or luna == '5' or luna == '7' or luna == '8' or luna == '10' or luna == '12':
            return "Luna introdusa are 31 de zile"
        elif luna == '2':
            return "Luna introdusa are 28 de zile"
        else:
            return 'Luna introdusa are 30 de zile'
nr = calendar(input('Introduceti o luna din an in forma de numar: '))
print(nr)


def cal(luna):
    import calendar
    rasp = calendar.monthrange(2021,luna)
    return f"Luna introdusa are {rasp[1]}"
month = cal(int(input('Luna:')))
print(month)
'''
'''

#Ex12

12. Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ",a )
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    d = int(input('d = '))



def calculatro(nr1,nr2):
    suma = nr1 + nr2
    diferenta = nr1 - nr2
    inmultirea = nr1 * nr2
    impartirea = nr1 / nr2
    return suma,diferenta,impartirea,impartirea

entry1 =int(input('nr1 = '))
entry2 =int(input('nr2 = '))

a,b,c,d = calculatro(entry1,entry2)

print("Suma: ",a )
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


#Ex13



def numere(*args):
    my_dict = {}
    for elem in range(len(args)):
        my_dict[args[elem]] = args.count(args[elem])
    return my_dict

rasp = numere(1,2,3,4,4,2)
print(rasp)

'''

