'''
#Ex1
def numar(nr):
    for elem in range(1,nr):
        print(elem)

numar(5)


#Ex2
def numar(nr):
    n = []
    for elem in range(1,nr):
        n.append(elem)
    return n

l = numar(5)
print(l)

#Ex3

def numere(x,y=2):
    s = x**y
    return f"The result of x={x} to the power of y={y} is:{s}"

rasp = numere(5,4)
print(rasp)

#Ex4
# Write a function that has one string argument and creates a substring made of the first, middle and last character of the string
# e.g.:  substring('Michael') => 'Mhl'
#        substring('Adrian')  => 'Arn' / 'Ain' (either one works)


def s(name):
    name_2=name[0]+name[len(name)//2]+name[len(name)-1]
    print(name_2)

s('Bogdan')

#Ex5

# Given 2 strings as arguments s1 and s2, write a function that appends s2 in the middle of s1
# e.g.:  append_middle('Legendary', 'wait')  => 'Legewaitndary'
#        append_middle('mama', 'MIA')  =>  'maMIAma'

def string(s1,s2):
    str2=s1[0:len(s1)//2]+s2+s1[len(s1)//2:]
    print(str2)
string('mama', 'MIA')


#Ex6

# Write a function that takes any number of string arguments and will return the string formed
# from the arguments separated by -
# e.g.: coma_separated('one', 'two', 'three') => 'one-two-three'
# coma_separated('one', 'two', 'three', 'four', 'five') => 'one-two-three-four-five'

def coma_separated(*args):
    rezultat = ""
    for elem in args:
        rezultat += elem + '-'
    return rezultat[:-1]

separated = coma_separated('one', 'two', 'three', 'four', 'five')
print(separated)

def coma_separated2(*args):
    rezultat2 = '-'.join(args)
    print(rezultat2[:-1])

separated = coma_separated('one', 'two', 'three', 'four', 'five')
print(separated)


#Ex7
def is_prime(nr):
    if nr / 2 == nr // 2:
        return False
    else:
        return True
s=is_prime(7)
print(s)

'''

#Ex8
def list_of_pime_in_interval(nr1, nr2):
    if nr1 / 2 == nr1 // 2:
        return

a = list_of_pime_in_interval(3, 31)
print(a)