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

h = Hissi(1, 20)
kerros = 17
print(f"Hissi siirtyy kerrokseen {kerros}")
h.siirry_kerrokseen(kerros)
print("Palataan alimpaan kerrokseen: ")
h.siirry_kerrokseen(h.alin)