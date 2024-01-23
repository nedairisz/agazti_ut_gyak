from greenaway_o import Film

def beolvas():
    fajl=open("greenaway.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    lista=[]
    for i in range(0, len(nyers_lista),1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split("-")
        cim=sor_tag[0]
        ev=sor_tag[1]
        film=Film(cim, ev)
        lista.append(film)
    return lista

def filmek_szama(lista):
    print(f"\tA filmek szama: {len(lista)}")

def szo(lista):
    for i in range(0,len(lista),1):
        if lista[i]=="szakács":
            print("Van olyan film, amiben szerepel a “szakács” szó")
        else:
            print("Nincs olyan film, amiben szerepel a “szakács” szó")