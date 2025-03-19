class kart():
    def __init__(self,kartno,sure):
        self.kartno = kartno
        self.sure = sure
         
    def kartSureHesabi(self):
        if kart.sure == 24:
            print("Kart süreniz doldu")
        else: 
            return True

    def abonmankontrol(self,kartno):
        if kartno<= 200 and kartno >= 100:
            return True
        else:
            return False
            
    def nakitkontrol(self,nakit):
        if nakit == 50:
            return True
        else: 
            return False
   
    def gunubirlikontrol(self,kartno):
        if kartno < 100 and kartno >= 0:
            kart.kartSureHesabi()
        else:
            return False