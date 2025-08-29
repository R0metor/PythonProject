import math
def funktio(halkaisija_cm, hinta_e):
    sade_cm = halkaisija_cm / 2
    pintaalacm2 = math.pi * (sade_cm ** 2)
    pintaalam2 = pintaalacm2 / 10000
    return hinta_e / pintaalam2

a1 = float(input("Anna 1 pizzan halkaisija cm: "))
a2 = float(input("Anna 1 pizzan hinta €: "))

b1 = float(input("Anna 2 pizzan halkaisija cm: "))
b2 = float(input("Anna 2 pizzan hinta €: "))

e1 = funktio(a1, a2)
e2 = funktio(b1, b2)

print(f"Ekan pizzan yksikköhinta: {e1:.2f} €/m^2")
print(f"Tokan pizzan yksikköhinta: {e2:.2f} €/m^2")

if e1 < e2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
elif e2 < e1:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    ("Molemmat pizzat ovat saman hintaisia")