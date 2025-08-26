import random

N = int(input("Kuinka monta pistettä: "))
osumat = 0
for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if y*y + x*x < 1.0:
        osumat += 1

pilikiarvo = 4*osumat/N

print("Piin likiarvo on", pilikiarvo)