class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusauto = Auto("ABC-123", 200)
print(f"Uuden auton ominaisuudet rekkari: {uusauto.rekisteritunnus}, huippunopeus {uusauto.huippunopeus} km/h")