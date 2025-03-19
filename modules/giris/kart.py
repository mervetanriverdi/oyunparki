class Kart:
    def __init__(self, kartno, sure):
        self.kartno = kartno  
        self.sure = sure      

    def kartSureHesabi(self):
        if self.sure >= 24:
            print("Kart süreniz doldu.")
            return False
        return True

    def abonmankontrol(self):
        if 100 <= self.kartno <= 200:
            print(f"{self.kartno} numaralı abonman kart geçerli.")
            return True
        print("Geçersiz abonman kart.")
        return False

    def nakitkontrol(self, nakit):
        if nakit == 50:
            print("Nakit ödeme alındı.")
            return True
        print("Yalnızca 50 TL kabul ediliyor.")
        return False

    def gunubirlikontrol(self):
        if 0 <= self.kartno < 100 and self.kartSureHesabi():
            print(f"{self.kartno} numaralı günübirlik kart geçerli.")
            return True
        print("Geçersiz günübirlik kart veya süresi dolmuş.")
        return False
