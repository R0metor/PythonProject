luku = int(input("Kokonaisluku: "))

if luku < 2:
    print(luku, "ei ole alkuluku")
else:
    on_alkuluku = True
    for i in range(2, int(luku**0.5)+1):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(luku, "on alkuluku")
    else:
        print(luku, "ei ole alkuluku")