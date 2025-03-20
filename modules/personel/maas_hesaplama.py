class Personel:
    def __init__(self, ad, soyad, pozisyon):
        self.ad = ad
        self.soyad = soyad
        self.pozisyon = pozisyon

    def maas_hesapla(self):
 if self.pozisyon.lower() == "müşteri destek":
            return 20000
        elif self.pozisyon.lower() == "oyun bakım":
            return 22000
        else:
            return 0
    def __str__(self):
        """
        Personelin bilgilerini yazdırır.
        """
        return f"{self.ad} {self.soyad} ({self.pozisyon}) - Maaş: {self.maas_hesapla()} TL"
