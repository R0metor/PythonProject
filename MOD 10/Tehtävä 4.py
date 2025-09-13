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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.tunnit = 0

    def tunti_kuluu(self):
        for a in self.autot:
            a.kiihdytä(random.randint(-10, 15))
            a.kulje(1)
        self.tunnit += 1
    def tulosta_tilanne(self):
        autot_jarjestyksessa = sorted(autot, key=lambda a: a.kuljettu_matka, reverse=True)
        otsikot = ("Rekisteri", "Huippu (km/h)", "Nopeus(km/h)", "Kuljettu (km)")
        rivi = "{:<8} {:>13} {:>14} {:>13}"
        print(rivi.format(*otsikot))
        for a in autot_jarjestyksessa:
            print(rivi.format(a.rekisteritunnus, a.huippunopeus, a.nopeus, f"{a.kuljettu_matka:.1f}"))
    def kilpailu_ohi(self):
        return any(a.kuljettu_matka >= self.pituus for a in self.autot )



autot = [Auto(f"ABC-{i}", random.randint(100,200)) for i in range (1, 11)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while True:
    kilpailu.tunti_kuluu()
    if kilpailu.tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
    if kilpailu.kilpailu_ohi():
        break
kilpailu.tulosta_tilanne()
print("Kilpailu ohi")
voittaja = max(kilpailu.autot, key=lambda a: a.kuljettu_matka)
print(f"Voittaja on: {voittaja.rekisteritunnus} {voittaja.kuljettu_matka:.0f} km")






