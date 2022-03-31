#Ex1
# O variabila este o locatie ce ii putem da noi valori si nume

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
var = b[0]
c = b[0]+b[1:-1].replace(var,var.upper()) + b[-1]
print(c)

#Ex19
#user = input('introduceti un nume de utilizator: ')
#parola = input('introduceti parola: ')
#l = (len(parola))
#nr = l * '*'
#print(f'Parola pt user este {nr} si are {l} caractere')






P = 'Corla is either the stupidest animal or the smartest rock'
print(P.count('the'))



#ex2 Tema refacuta a 2 oara

x = 'nume'
y = 10
z = 2.5
adevar = True


#Ex3

print(type(x))
print(type(y))
print(type(z))
print(type(adevar))



#Ex4
z = 2.5
z = round(z)
print(type(z))




#Ex5

Nume = 'Bogdan'
varsta = 27
Inaltime = 1.75
Sex_masculin = True

print('Numele meu este '  +Nume)
print(f'Am varsta de {varsta} ')
print(f'O inaltime de  {Inaltime}')
print(f'Si sunt de sex Masculin: {Sex_masculin}')




#Ex6

x = input(' nume=  ')
y = input('prenume=  ')
nume = x + y
l = len(nume)

print(f'Numele complet are {l} Caractere')




#Ex7

x = int(input(' x=  '))
y = int(input(' y=  '))
aria = x*y

print(aria)



#Ex8

x = int(input('Adauga un nr:  '))
str = 'Coral is either the stupidest animal or the smartest rock'

print(str[:-x])


#Ex9

str = 'Coral is either the stupidest animal or the smartest rock'
x = str[:5]+str[-5:]
print(x)


#Ex10

str = 'Coral is either the stupidest animal or the smartest rock'
x = str.split(' ')
print(x.count('the'))



#Ex11
str = 'Coral is either the stupidest animal or the smartest rock'
print(str.replace(' the ',' THE '))




#EX12
str = 'Coral is either the stupidest animal or the smartest rock'
x = str.find('rock')
print(x)



#Ex13

Nume = 'Bogdan'
Varsta = 27
Inaltime = 1.75
Sex_masculin = True

str = Nume+str(Varsta)+str(Inaltime)+str(Sex_masculin)
print(f'Numele meu este {Nume},am varsta de {Varsta} anii , o inaltime de {Inaltime}m , si sunt de sexul Masculin /{Sex_masculin}.')



#Ex14
x = '0123456789'
print(x[::2]) # Par
print(x[1::2]) # Impar



#Ex15
L = int(input('Adaugati o Latime:'))
l = int(input('Adaugati o lungime:'))
aria = L * l
print( f'Aria este de {aria}m2')




#Ex16

s = input('s:')
print(s[len(s)//2])



#Ex17
a,b = input('Tastati 2 cuvinte:').split()
print(a)
print(b)




#EX18


x = input('Tastati:')
b = x[0]
c = x [0] + x [1:-1].replace(b,b.upper())+x[-1]
print(c)

#EX19
user = input('user:')
pas = input('pass:')
l = len(pas)
nr = l * '*'
print(f'Parola {nr}  contine {l} ')