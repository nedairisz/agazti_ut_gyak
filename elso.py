def bekeres():
    szo1= input("\tKerek egy szot: ")
    szo2= input("\tKerek egy masik szot: ")
    print("I/a.")
    if len(szo1)>len(szo2):
        print(f"\tA hosszabb szo: {szo1}")
    elif len(szo1)<len(szo2):
        print(f"\tA hosszabb szo: {szo2}")
    else:
        print("\tHosszuk egyenlo.")
    print("I/d.")
    kul=abs(len(szo1)-len(szo2))
    print(f"\tA szavak hosszanak kulonbsege: {kul}")