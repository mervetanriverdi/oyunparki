from kart import abonmankontrol, nakitkontrol, gunubirlikontrol

class Giris:
    def __init__(self, kart):
        self.kart = kart

    def giris(self):
        print("\nGiriş Tipi Seçin:")
        print("1: Abonman")
        print("2: Nakit")
        print("3: Kart ile Günübirlik")
        
        try:
            giris_tipi = int(input("Seçiminiz: "))

            if giris_tipi == 1:
                kartno = int(input("Kart numarası girin: "))
                if abonmankontrol(kartno):
                    print("Abonman girişi başarılı.")
                else:
                    print("Abonman geçersiz veya süresi dolmuş.")

            elif giris_tipi == 2:
                miktar = int(input("50 TL verin (sadece 50 TL kabul edilir): "))
                if nakitkontrol(miktar):
                    print("Nakit girişi başarılı.")
                else:
                    print("Yetersiz veya hatalı ödeme.")

            elif giris_tipi == 3:
                kartno = int(input("Kart numarası girin: "))
                if gunubirlikontrol(kartno):
                    print("Günübirlik giriş başarılı.")
                else:
                    print("Günübirlik kart geçersiz.")

            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
