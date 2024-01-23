import random

def szamlista():
    lista=[]
    print(f"\t", end="")
    for i in range(0,15,1):
        szam:int=random.randint(100, 200)
        lista.append(szam)
        if i==14:
            print(szam, end="")
        else:
            print(szam, end="%")
    return lista

def legkisebb(lista):
    lk=0
    for i in range(0,len(lista),1):
        if lista[lk]>lista[i]:
            lk=i
    return lk

def kiir(lk):
    fajl=open("legkisebb.txt", "w", encoding="utf-8")
    fajl.write(f"\tA legkisebb elem: {lista[lk]}")