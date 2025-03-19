class NobetCizelgesi:
    def __init__(self, personel_adi, soyadi):
        self.personel_adi = personel_adi
        self.soyadi = soyadi
        self.nobet_gunleri = []  # Nöbet günleri listesi

    def nobet_ekle(self, gun):
       
        if gun not in self.nobet_gunleri:
            self.nobet_gunleri.append(gun)
    
    def nobet_sil(self, gun):
       
        if gun in self.nobet_gunleri:
            self.nobet_gunleri.remove(gun)

    def __str__(self):
        return f"{self.personel_adi} {self.soyadi} - Nöbet Günleri: {', '.join(self.nobet_gunleri)}"
