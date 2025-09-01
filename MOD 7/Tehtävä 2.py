nimet = set()
while True:
    a = input("Anna nimi:")
    if a == "":
        for nimi in nimet:
            print(nimi)
        break
    if a in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(a)