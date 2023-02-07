
from pojisteny import Pojisteny


class HledaniPojisteneho(Pojisteny):
    def __init__(self, jmeno, prijmeni, vek, telefon):
        super().__init__(jmeno, prijmeni)
        self.kartoteka_pojistencu = []
        self.hledat_jmeno = jmeno
        self.hledat_prijmeni = prijmeni



