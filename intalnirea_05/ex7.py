
#Ex7 7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y

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

