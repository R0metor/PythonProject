import random
kuutiot = int(input("Anna arpakuutioiden määrä: "))
summa = 0
for i in range(kuutiot):
    summa += random.randint(1, 6)
print("Arpakuutioiden summa: ", summa)