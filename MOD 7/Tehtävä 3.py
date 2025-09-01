kentat = {}
while True:
    a = int(input("Syötä uusi lentoasema 1 haku 2 lopeta 3: "))
    if a == 1:
        icao = input("ICAO koodi: ")
        nimi = input("Lentokentän nimi: ")
        kentat[icao] = nimi
    elif a == 2:
        koodi = input("ICAO koodi: ")
        print(kentat[koodi])
    elif a == 3:
        break