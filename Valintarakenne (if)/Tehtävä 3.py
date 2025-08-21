sukupuoli = input("Sukupuoli: ")
hemogl = int(input("Hemoglobiiniarvo: "))

if sukupuoli == "mies":
    if hemogl < 134:
        print("Hemoglobiini arvo on alhainen")
    elif hemogl > 195:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini on normaali")

elif sukupuoli == "nainen":
    if hemogl < 117:
        print("Hemoglobiini arvo on alhainen")
    elif hemogl > 175:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini on normaali")