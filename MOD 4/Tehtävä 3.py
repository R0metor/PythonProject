luvut = []
while True:
    numero = input("numero: ")
    if numero == "":
        if luvut:
            print("Suurin:", max(luvut))
            print("Pienin:", min(luvut))
        break
    a = float(numero)
    luvut.append(a)