#Ex1
'''
note = ['do','re','mi','fa','sol','la','si','do']
note2 = note[::-1]
print(note)
print(note2)
note.reverse()
print(note)



#Ex2
print(note.count('do'))



#EX3

a = [3,1,0,2]
b = [6,5,4]
print(a+b)
a.extend(b)
print(a)



#Ex4
a = [3,1,0,2]
b = [6,5,4]
c = a + b
c.sort()
print(c)
c.remove(0)
print(c)


#EX5

if len(c) <= 0:
    print('Lista este goala ')
else:
    print('Lista nu este goala ')

#EX6
c.clear()
print(c)

#Ex7
if len(c) <= 0:
    print('Lista este goala ')
else:
    print('Lista nu este goala ')

#Ex8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

#Ex9
print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Ana a luat nota {dict1["Gigel"]}')
print(f'Ana a luat nota {dict1["Dorel"]}')

for key in dict1:
    print(f"{key} a luat nota {dict1[key]}")

#Ex10
dict1["Dorel"] = 6
print(dict1)

#Ex11
del dict1['Gigel']
print(dict1)

dict1["Ionica"] = 9
print(dict1)


#Ex12
zile_sapt = {'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('Luni')
print(zile_sapt)


if weekend & zile_sapt == weekend:
    print('Weekend este un subset in zilele saptamani')
else:
    print('Weekend nu este un subset in zilele saptamani')

if weekend.issubset(zile_sapt):
    print("Este")
else:
    print("nu este ")

print(zile_sapt ^ weekend)
print(zile_sapt & weekend)


#ex16

poli = ['Bogdan','Titi','Ancuta','Florina','Mihai']
schimbari_max = 3
iasa = input('Cine iasa de pe teren? : ')

if iasa in poli:
    intra = input('Alege cine sa intre ')
    poli.append(intra)
    poli.pop(poli.index(iasa))
    schimbari_max = schimbari_max -1
    print(f'Schimbare efectuata , a iesit {iasa} si a intrat {intra}')
    print(f'Schimbari disponibile {schimbari_max}')

else:

    print('Jucatorul nu este pe Teren ')



#Ex17
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a = []
for fruit in fruits:
    if 'e' in fruit:
        a.append(fruit)
print(a)





#EX18

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a = []
for fruit in fruits:
    if len(fruit) == 6:
        a.append(fruit)
print(a)
'''

