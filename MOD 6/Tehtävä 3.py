def muunnin(gallona):
    return gallona*3.785

while True:
    bensa = float(input("Anna gallonamäärä: "))
    if bensa < 0:
        break
    else:
        print(f"{bensa:.2f} gallonaa on {muunnin(bensa):.2f} litraa")
