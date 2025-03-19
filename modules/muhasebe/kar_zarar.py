class KarZarar:
    def __init__(self, gelir, gider):
self.gelir = gelir
        self.gider = gider


 def kar_zarar(self):
        return self.gelir - self.gider


    def __str__(self):



         return f"Gelir: {self.gelir} TL, Gider: {self.gider} TL, Kar/Zarar: {self.kar_zarar()} TL"
