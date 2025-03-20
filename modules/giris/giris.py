from kart import abonmankontrol, nakitkontrol, gunubirlikontrol
class Giris():

    def __init__(self,kart):
        self.kart = kart

    def giris(self):    
        giristipi = int(input("Giriş tipi belirtin(1:abonman 2:nakit 3:kart ile günübirlik): "))
        if giristipi == 1:
            kartno = int(input("kart no girin:"))
            abonmankontrol(kartno)
        if giristipi == 2:
            nakit = int(input("lütfen 50 tl verin. sadece 50 tl paraüstü vermiyoruz alana da almıyoruz."))
            nakitkontrol(nakit)
        if giristipi == 3:
            kartno = int(input("kart no girin:"))
            gunubirlikontrol(kartno)
        