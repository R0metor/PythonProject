a = 0
ss = "rules"
kt = "python"
while True:
    syote = input("Syötä käyttäjätunnus: ")
    syote2 = input("Syötä salasana: ")
    if syote == kt:
        if syote2 == ss:
            print("Tervetuloa")
            break
    elif syote != kt or syote2 != ss:
        a +=1
        if a >= 5:
            print("Pääsy evätty")
            break