vuosi = int(input("Vuosi: "))

if (vuosi % 400 == 0) or (vuosi % 4 == 0) and (vuosi % 100 != 0):
    print(vuosi, "on karkausvuosi")
else:
    print(vuosi, "ei ole karkausvuosi")