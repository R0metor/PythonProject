class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

auto = Auto("ABC-123", 200)
for muutos in (30, 70, 50):
    auto.kiihdytä(muutos)
    print(f"Nopeus muutoksen {muutos:+} km/h jälkeen: {auto.nopeus} kmh/h")

auto.kiihdytä(-200)
print(f"Hätäjarrutuksen jälkeen: {auto.nopeus} km/h")