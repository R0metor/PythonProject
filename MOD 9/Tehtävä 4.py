import random
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

autot = [
    Auto(f"ABC-{i}", random.randint(100,200))
    for i in range (1, 11)
]
tuntimäärä = 0
maali = 10000

while max(a.kuljettu_matka for a in autot) < maali:
    for a in autot:
        a.kiihdytä(random.randint(-10, 15))
    for a in autot:
        a.kulje(1)
    tuntimäärä += 1

autot_jarjestyksessa = sorted(autot, key=lambda a: a.kuljettu_matka, reverse=True)
voittaja = autot_jarjestyksessa[0]

otsikot = ("Rekisteri", "Huippu (km/h)", "Nopeus(km/h)", "Kuljettu (km)")
rivi = "{:<8} {:>13} {:>14} {:>13}"
print(f"\nKilpailu päättyi {tuntimäärä} tunnin jälkeen. Voittaja: {voittaja.rekisteritunnus}\n")
print(rivi.format(*otsikot))
for a in autot_jarjestyksessa:
    print(rivi.format(a.rekisteritunnus, a.huippunopeus, a.nopeus, f"{a.kuljettu_matka:.1f}"))
