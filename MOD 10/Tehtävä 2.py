class Hissi:
    def __init__(self, alinkerros: int, ylinkerros: int):
        self.alin = alinkerros
        self.ylin = ylinkerros
        self.nykyinen = alinkerros

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kerros: int):
        if kerros < self.alin:
            kerros = self.alin
        if kerros > self.ylin:
            kerros = self.ylin

        while self.nykyinen < kerros:
            self.kerros_ylös()
        while self.nykyinen > kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alinkerros: int, ylinkerros: int, hissit: int):
        self.alin = alinkerros
        self.ylin = ylinkerros
        self.hissit = [Hissi(alinkerros, ylinkerros) for _ in range(hissit)]

    def aja_hissiä(self, hissi: int, kerros: int):
        id = hissi - 1
        print(f"Ajetaan hissi {hissi} kohti kerrosta {kerros}:")
        self.hissit[id].siirry_kerrokseen(kerros)

    def tulosta_tilanne(self):
        for z, x in enumerate(self.hissit, start=1):
            print(f"Hissi {z}: kerros {x.nykyinen}")


talo = Talo(1, 20, 7)
talo.tulosta_tilanne()
talo.aja_hissiä(1, 16)
talo.aja_hissiä(4, 9)
talo.aja_hissiä(2, 20)
talo.tulosta_tilanne()