kuha = int(input("Kuhan pituus: "))
if kuha < 37:
    print("Laske kuha takaisin järveen se on", 37-kuha,"senttiä liian lyhyt")
elif kuha >= 37:
    print("Nice catch!")