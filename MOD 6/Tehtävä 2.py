import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Nopan maksimisilmäluku: "))

while True:
    tulos = noppa(maksimi)
    print(f"Tulos {tulos}")
    if tulos == maksimi:
        print("Saatiin maksimi")
        break