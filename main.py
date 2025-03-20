from modules.giris.giris import Giris
from modules.giris.kart import Kart
from modules.muhasebe.harcamalar import harcama_ekle
from modules.muhasebe.kar_zarar import hesapla_kar_giderler
from modules.personel.izin_yonetimi import IzinYonetimi
from modules.personel.maas_hesaplama import Personel
from modules.personel.nobet_cizelgesi import NobetCizelgesi
from modules.oyunalani.binis import Binis

if __name__ == "__main__":
    kartno = int(input("Kart numaranızı girin: "))
    sure = int(input("Kart süresini girin (saat): "))
    kart = Kart(kartno, sure)
    giris_sistemi = Giris(kart)
    giris_sistemi.giris()

    binis_sistemi = Binis()
    binis_sistemi.Binisverisi()
    binis_sistemi.DosyadanOkuma()

    personel = Personel("Ahmet", "Yılmaz", "müşteri destek")
    print(personel)

    nobet = NobetCizelgesi("Mehmet", "Demir")
    nobet.nobet_ekle("Pazartesi")
    nobet.nobet_ekle("Cuma")
    print(nobet)

    izin = IzinYonetimi("Ayşe", "Kaya")
    izin.izin_ekle("Salı")
    print(izin)

    harcama = harcama_ekle("malzeme", 5000, "2025-03-19")
    print("Harcama:", harcama)

    kar = hesapla_kar_giderler(100000, 45000)
    print("Net Kar:", kar)
