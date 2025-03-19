class Giris:
    def __init__(self, kontrolcüler):
        self.kontrolcüler = kontrolcüler

    def giris(self):
        print("\nGiriş Tipi Seçin:")
        print("1: Abonman")
        print("2: Nakit")
        print("3: Kart ile Günübirlik")
        
        try:
            giris_tipi = int(input("Seçiminiz: "))
            if giris_tipi == 1:
                kartno = int(input("Kart numarası girin: "))
                if self.kontrolcüler.abonmankontrol():
                    print("✅ Giriş başarılı.")

            elif giris_tipi == 2:
                miktar = int(input("50 TL verin (sadece 50 TL kabul edilir): "))
                if self.kontrolcüler.nakitkontrol(miktar):
                    print("Giriş başarılı.")

            elif giris_tipi == 3:
                kartno = int(input("Kart numarası girin: "))
                if self.kontrolcüler.gunubirlikontrol():
                    print(" Giriş başarılı.")

            else:
                print("Geçersiz seçim, tekrar deneyin.")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
