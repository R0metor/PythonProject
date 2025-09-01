kevät = (3, 4, 5)
kesä = (6, 7, 8)
syksy = (9, 10, 11)
talvi = (12, 1, 2)
a = int(input("Syötä kuukautesi numero: "))
if a in kevät:
    print("Kevät")
elif a in kesä:
    print("Kesä")
elif a in syksy:
    print("Syksy")
elif a in talvi:
    print("Talvi")
else:
    print("Luku ei ole kuukausi")