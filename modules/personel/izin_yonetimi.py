class IzinYonetimi:
    def __init__(self, personel_adi, soyadi):
        self.personel_adi = personel_adi
        self.soyadi = soyadi
        self.izin_gunleri = []  # İzin günleri listesi

    def izin_ekle(self, gun):
        """Bir personel için izin günü ekler."""
        if gun not in self.izin_gunleri:
            self.izin_gunleri.append(gun)
    
    def izin_sil(self, gun):
        """Bir personelin izin gününü siler."""
        if gun in self.izin_gunleri:
            self.izin_gunleri.remove(gun)

    def __str__(self):
        return f"{self.personel_adi} {self.soyadi} -İzin Günleri: {', '.join(self.izin_gunleri)}"
