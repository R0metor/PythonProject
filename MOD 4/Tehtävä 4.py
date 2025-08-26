import random
luku = random.randint(1,10)
while True:
    arvaus = int(input("Anna luku 1 ja 10 väliltä: "))
    if arvaus == luku:
        print("Oikein")
        break
    elif arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")
