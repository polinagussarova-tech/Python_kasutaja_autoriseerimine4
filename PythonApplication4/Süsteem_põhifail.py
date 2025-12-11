from MyModule import *

k=['Mari', 'Juku', 'Kati']
s=['1234', '5678', 'abcd']

while True:
    print("Vali tegevus: ")
    print("1- registreerimine")
    print("2- autoriseerimine")
    print("3- paroolivahetus")
    print("4- paroolitaastamine")
    print("5- välju")

    valik=input("Sisesta valik (1-5): ")
    if valik=='1':
        registreerimine(k, s)
    elif valik=='2':
        autoriseerimine(k, s)
    elif valik=='3':
        paroolivahetus(k, s)
    elif valik=='4':
        paroolitaasramine(k, s)
    elif valik=='5':
        print("Väljun programmist.")
        break
    else:
        print("Vigane valik, proovi uuesti.")