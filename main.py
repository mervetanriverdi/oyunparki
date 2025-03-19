from giris import Giris
from kart import Kart

if __name__ == "__main__":
    kartno = int(input("Kart numaranızı girin: "))
    sure = int(input("Kart süresini girin (saat): "))
    
    kart = Kart(kartno, sure)  
    giris_sistemi = Giris(kart) 
    giris_sistemi.giris()