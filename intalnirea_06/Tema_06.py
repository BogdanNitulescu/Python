'''
#ex 1

#Clasa Cerc

#Atribute: raza, culoare

#Constructor pt ambele atribute

#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria
#diametru()
#circumferinta()

import math
class cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def aria(self):
            return  f'Raza cercului este {3.14 * self.raza * self.raza}'

    def diametru(self):
        return  f'Diametru cercului este {self.raza * 2}'

    def circumferinta(self):
        return f'Circumferinta este de {2 * math.pi * self.raza}'

    def descrie_cerc(self):
        return f"culoare = {self.culoare} , raza = {self.raza}"

metode = cerc(14,'Rosu')
print(f'Descriere cerc :  {metode.descrie_cerc()}')
print(f' Aria {metode.aria()}')
print(f' Aria {metode.diametru()}')
print(f' Aria {metode.circumferinta()}')


#Ex2

#Clasa Dreptunghi

#Atribute: lungime, latime, culoare

#Constructor pt toate atributele

#Metode:
#descrie() va PRINTA lungime, latime, culoare
#aria()
#perimetrul()
#schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class dreptunghi:
    def __init__(self, lungime, latime, input_culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = input_culoare

    def descrie_dreptunghi(self):
        return f"Latime : {self.latime},Lunghime : {self.lungime}, culoare: {self.culoare} "

    def aria_dreptunghi(self):
        return f'Aria = {self.lungime * self.latime}'

    def perimetru_dreptunghi(self):
        return f'Perimetru = {2 * (self.lungime * self.latime)}'

    def noua_culoare(self,culoare):
        self.culoare = culoare
        return f'Noua culoare este {self.culoare}'
rasp = dreptunghi(6,5,'Verde')
print(rasp.descrie_dreptunghi())
print(rasp.aria_dreptunghi())
print(rasp.perimetru_dreptunghi())
print(rasp.noua_culoare('Rosu'))


#Ex3

#Clasa Angajat

#Atribute: nume, prenume, salariu

#Constructor() pt toate atributele // constructor reprezinta __init__

#Metode:
#descrie() print nume, prenume, salariu
#nume_complet()
#salariu_lunar()
#salariu_anual()
#marire_salariu(procent)

class angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return f' Angajatul {self.nume} {self.prenume} , are salariul de {self.salariu}!'

    def nume_complet(self):
        return f'Numele complet este {self.nume} {self.prenume}'

    def salariu_lunar(self):
        return f'Salariul lunar este de {self.salariu}'

    def salaiu_anual(self):
        return f'Salariu anual este de {self.salariu * 12}'

    def marire_salariu(self):
        marire = int(input('Introdu un procentaj de marire al salariului: '))
        return f'Salariul sa marit cu {marire}% si acuma este de {self.salariu + self.salariu *(marire / 100)}'

rasp2 = angajat('Bogdan','Mihai',3500)
print(rasp2.descriere())
print(rasp2.nume_complet())
print(rasp2.salariu_lunar())
print(rasp2.salaiu_anual())
print(rasp2.marire_salariu())




#Ex4
import datetime
class factura:
    def __init__(self, serie,input_numar,input_produs,input_cantitate,input_pret_buc):
        self.serie= serie
        self.numar = input_numar
        self.produs = input_produs
        self.cantitate = input_cantitate
        self.pret_buc = input_pret_buc


    def factura2(self):
        return f'Facutra seria {self.serie} numar {self.numar}'


    def data(self):
        data_exacta = datetime.datetime.now()
        return f'Data {str(data_exacta)[:10]}'


    def numar_telefon(self,numar2,produs2,cantitate2,pret_buc2):
        self.numar2 = numar2
        self.produs2 = produs2
        self.cantitate2 = cantitate2
        self.pret_buc2 = pret_buc2

        return f'| {self.numar2}  |{self.produs2} |  {self.cantitate2}  |  {self.pret_buc2}lei   | {self.cantitate2 * self.pret_buc2}'

rasp3 = factura('TM',1,'RedBull',2,'7Lei')
print(rasp3.factura2())
print(rasp3.data())
print(f'|Numar Telefon|   Produs  |   Cantitate  |   Pret Bucata  | Tota')
print(rasp3.numar_telefon('0723065313','Ciocolata',3,8))
print(rasp3.numar_telefon('0742523913','Apa',2,3))





#Ex5

class cont:
    def __init__(self, import_iban, import_titular_cont, import_sold):
        self.iban = import_iban
        self.titular_cont = import_titular_cont
        self.sold = import_sold

    def afisare_sold(self):
        return  f"Titularul {self.titular_cont} are in cont suma de {self.sold} lei !"

    def debitare_cont(self):
        debitare = int(input(f"Sold disponibil {self.sold} Lei, Retragi suma de :  "))
        return f'Sa retras suma de {debitare} Lei , sold disponibil {self.sold - debitare} Lei'

    def creditare_cont(self):
        pass

rasp4 = cont('ContSalarial','Nitulescu Bogdan',3500)
print(rasp4.afisare_sold())
print(rasp4.debitare_cont())




'''

#Ex6

class masina:

    def __init__(self,marca, input_model, input_viteza_maxima,viteza_actuala,culoare,culori_disponibie,inmatriculata):
        self.marca = marca
        self.model = input_model
        self.viteza_maxima = input_viteza_maxima
        self.viteza_actuala = viteza_actuala
        self.culoare = culoare
        self.culori_disponibile = culori_disponibie
        self.inmatriculata = inmatriculata

    def descriere(self):
        print(f'Marca {self.marca}, model {self.model} , are viteza maxima de {self.viteza_maxima} km/h,acuma avem {self.viteza_actuala} km/h , are culoare {self.culoare} , inmatriculare {self.inmatriculata}!')

    def inmatriculare(self):
        print(f'Masina este inmatriculat {self.inmatriculata}')

    def revopsire(self,elem):
        culori_existente = {'Rosu','Albastru','Alb','Negru'}
        if elem in culori_existente:
            return f'Culoare noua {elem}'
        else:
            return f'Error'

    def accelereaza(self,viteza):
        if viteza < self.viteza_actuala:
            return f'Ati incetiti la {viteza} km/h'
        elif viteza <= self.viteza_maxima:
            self.viteza_actuala = viteza
            return f' {self.viteza_actuala} km/h '
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            return f'{self.viteza_actuala} km/h Viteza maxima'
        else:
            return 'error'

    def frana(self,frana):
        if frana == 'Frana':
            self.viteza_actuala = 0
            return f'Ati oprit , viteza actuala {self.viteza_actuala} km/h'
        else:
            return f'error'

rasp5 = masina('Audi','Q5',240,80,'Gri',{'Rosu','Albastru','Alb','Negru'},False)
rasp5.descriere()
rasp6 = masina('Audi','Q5',240,80,'Gri',{'Rosu','Albastru','Alb','Negru'},True)
rasp6.inmatriculare()
rasp7 = masina('Audi','Q5',240,80,'Alb',{'Rosu','Albastru','Alb','Maro','Negru'},True)
print(rasp7.revopsire('Alb'))
rasp8 = masina('Audi','Q5',240,80,'Alb',{'Rosu','Albastru','Alb','Maro','Negru'},True)
print(rasp8.accelereaza(300))
rasp9 = masina('Audi','Q5',240,80,'Alb',{'Rosu','Albastru','Alb','Maro','Negru'},True)
print(rasp9.frana('Frana'))

'''Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''


class TodoList:
    todo = {}

    def adaugare_task(self,nume,descriere):
        if nume not in self.todo:
            self.todo[nume] = descriere
            print(self.todo)

    def finalizare_task(self,nume):
        del self.todo[nume]
        print(self.todo)

    def afiseaza_todo_list(self):
        todo_list = self.todo.keys()
        print(todo_list)

    def afiseaza_detali_suplimentare(self,nume_task):
        if nume_task not in self.todo:
            r = input('Doriti sa adaugati task-ul in lista?  DA / NU : ')
            if r == 'DA':
                detalii_task = input('Introduceti detalii : ')
                self.adaugare_task(nume_task,detalii_task)
            else:
                print('La Revedere')
        else:
            print(f'Detalile taskului {nume_task} sunt : {self.todo[nume_task]}')

todo1 = TodoList()
todo1.adaugare_task('Task 1','Invata python')
todo1.adaugare_task('Task 2','Citeste')
todo1.adaugare_task('Task 3','ScrieCod')
todo1.finalizare_task('Task 2')
todo1.afiseaza_todo_list()
todo1.afiseaza_detali_suplimentare('Task 5')