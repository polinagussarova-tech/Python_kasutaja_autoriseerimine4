#Registreerimine

k=[]
s=[]

def registreerimine(k:list, s:list)->any:
    kasutajanimi=input("Sisesta kasutajanimi: ")
    if kasutajanimi in k:
        return

    parool=input("Sisesta parool: ")

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

        print("Sisesta uus parool: ")
    else:
        print("Head aega")

def paroolitaasramine(k:list, s:list)->any:
    pass