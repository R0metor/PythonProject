import random
def laskin(lista):
    return sum(lista)

numerot = []

for i in range(15):
    numerot.append(random.randint(1, 100))

print(f"Lukujen summa {laskin(numerot)}")

