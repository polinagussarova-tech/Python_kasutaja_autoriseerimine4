#Registreerimine

k=[]
s=[]

def registreerimine(k:list, s:list)->any:
    kasutajanimi=input("Sisesta kasutajanimi: ")
    if kasutajanimi in k:
        print("Selline kasutaja on juba olemas!")
        return

    vastus=input("Valige 1, kui te soovite parooli ise luua või valige 2, kui soovite teha parooli genereerimise abil (1/2):")

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

            if number or lower or upper or symbol:
                print(f"Uus parool on {parool}")
                break

    elif vastus=="2":
        import random
        parool=""
        str1=".,:;!_*-+()/#¤%&"
        str2="0123456789"
        str3="qwertyuiopasdfghjklzxcvbnm"
        str4=str3.upper()

        kõik=str1+str2+str3+str4
        for i in range(12):
            parool += random.choice(kõik)

        print(f"Genereeritud parool:{parool}")
        

    else:
        print("Palun sisesta ainult 1 või 2!")
        return

    k.append(kasutajanimi)
    s.append(parool)
    print(k)
    print(s)

#Autoriseerimine

def autoriseerimine(k:list, s:list)->any:
    kasutajanimi=input("Sisesta kasutajanimi: ")
    if kasutajanimi not in k:
        print("Seda kasutaja ei ole!")
        return
    parool=input("Sisesta parool: ")

    i=k.index(kasutajanimi)
    if s[i]==parool:
        print("Sisselogitud!")
    else:
        print("Vale parool!")

    k.append(kasutajanimi)
    s.append(parool)
    print(k)
    print(s)

#Paroolivahetus

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

#Paroolitaastamine

def paroolitaastamine(k:list, s:list)->any:
    kasutajanimi = input("Sisesta kasutajanimi: ")

    if kasutajanimi in k:
        i=k.index(kasutajanimi)

        uus_parool=input("Sisesta uus parool: ")
        s[i]=uus_parool
        print("Parool taastatud!")

    else:
        print("Sellist kasutajanime pole!")

    k.append(kasutajanimi)
    s.append(uus_parool)
    print(k)
    print(s)