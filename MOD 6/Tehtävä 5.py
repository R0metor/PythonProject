import random
def uuslista(lista):
    return [x for x in lista if x % 2 == 0]

luvut = [random.randint(1, 100) for x in range(10)]
print("Alkuperäinen", luvut)
print("Uusi lista", uuslista(luvut))