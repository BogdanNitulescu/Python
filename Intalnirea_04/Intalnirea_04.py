# Given the lists: lst1 = ["Black", "White", "Red"] and lst2 = ["Red", "Green"].
# What do I write to get: "Black", "White" ? Using some relation between the 2 lists
#EX1
'''
lst1 = ["Black", "White", "Red"]
lst2 = ["Red", "Green"]
print(set(lst1)-set(lst2))


#Ex2
lst = [1,2,3,3,1,1,4,5,5]
lst_n = []
for n in lst:
    if n not in lst_n:
        lst_n.append(n)
print(f'{lst_n}')
'''

#Sa da o lista cu nume names_list = ["Valentina", "Raluca", Cristian", "Arthur", "Vlad", "Florina", "Dan", "Tudor", "Gabi"].
# Iterati lista, verificati daca numele incepe cu litera 'V', in caz afirmativ, sariti peste numele respectiv.
# In caz contrar afisati o structura de date formata din nume si indexul din lista unde a fost intalnit.

names_list = ["Valentina", "Raluca", "Cristian", "Arthur", "Vlad", "Florina", "Dan", "Tudor", "Gabi"]
#v1
for idx_nume,nume in enumerate(names_list):
    if nume[0] == 'V':
        continue
    print(nume,idx_nume)
#v2
for nume in names_list:
    if nume[0] == 'V':
        continue
    print(nume,names_list.index(nume))