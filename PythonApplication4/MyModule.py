#Registreerimine

from pickletools import string1


k=[]
s=[]

def registreerimine(k:list, s:list)->any:
    kasutajanimi=input("Sisesta kasutajanimi: ")
    if kasutajanimi in k:
        print("Selline kasutaja on juba olemas!")
        return

    küsimus=print(input("Kas te soovite reegistreerida?: (Jah/Ei) "))

    vastus=input("Valige 1, kui te soovite parooli ise luua või valige 2, kui soovite teha parooli genereerimise abil: (1/2) ")

    if vastus=="1":
        while True:
            parool=input("Sisesta parool: ")

            number=False
            lower=False
            upper=False
            symbol=False

            for t in parool:
                if t.isdigit():
                    number=True
                if t.islower():
                    lower=True
                if t.isupper():
                    upper=True
                if t in ".,:;!_*-+()/#¤%&":
                    symbol=True

            if number and lower and upper and symbol:
                print(f"Uus parool on {parool}")
                break
            else:
                print("Parool ei vasta tingimustele!")

    elif vastus=="2":
        import random

        str1=".,:;!_*-+()/#¤%&"
        str2="0123456789"
        str3="qwertyuiopasdfghjklzxcvbnm"
        str4=str3.upper()

        kõik=str1+str2+str3+str4
        parooll=""

        for i in range(12):
            parooll+=random.choice(kõik)

        print(f"Genereeritud parool:{parooll}")

    else:
        print("Palun sisesta ainult Jah või Ei!")
        return






    k.append(kasutajanimi)
    s.append(parool)



def autoriseerimine(k:list, s:list)->any:
    kasutajanimi=input("Sisesta kasutajanimi: ")
    if kasutajanimi not in k:
        return
    parool = input("Sisesta parool: ")

    i=k.index(kasutajanimi)
    if s[i]==parool:
        print("Sisselogitud!")
    else:
        print("Vale parool!")

def paroolivahetus(k:list, s:list)->any:
    vastus=input("Kas te tahate muuta parool? (Jah/Ei): ")
    if vastus=='Jah':
        kasutajanimi=input("Sisesta sinu kasutajanimi: ")

        if kasutajanimi in k:
            i=k.index(kasutajanimi)

            uus_parool=input("Sisesta uus parool: ")
            s[i]=uus_parool

            print("Parool muudetud")
        else:
            print("Vale kasutajanimi!")
    else:
        print("Head aega")

def paroolitaasramine(k:list, s:list)->any:
    kasutajanimi = input("Sisesta kasutajanimi: ")

    if kasutajanimi in k:
        i=k.index(kasutajanimi)
        uus_parool=input("Sisesta uus parool: ")
        s[i]=uus_parool
        print("Parool taastatud!")
    else:
        print("Sellist kasutajanime pole!")