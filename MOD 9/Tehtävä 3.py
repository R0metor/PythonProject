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

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += tuntimäärä * self.nopeus


auto = Auto("ABC-123", 200)
auto.kuljettu_matka = 2000
auto.kiihdytä(60)
auto.kulje(1.5)

print(f"Nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km/h")