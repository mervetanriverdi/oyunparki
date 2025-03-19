
class Binis():
    def __init__(self):
        self.sayac=0

    def Binisverisi(self):
        kontrol=int(input("Oyuncağa binecek misin? 1-Evet \n2-Hayır"))

        if kontrol==1:
            self.sayac+=1
            print(f"Binis verisi:{self.sayac}")
            with open("binis_verisi.txt","a") as file:
                 file.write(f"Binis Sayacı:{self.sayac}\n")

        elif kontrol==2:
                print("Oyuncağa binemezsin")

        else:
                print("Geçersiz seçim!") 

    def DosyadanOkuma(self):
        try:
            with open("binis_verisi.txt", "r") as file:  
                print("\nDaha önceki biniş verileri:")
                lines=file.readlines()
                toplam_binis=0

                for line in lines:
                     try:
                          toplam_binis+=int(line.strip())
                     except ValueError:
                          continue  
                print(f"Toplam Biniş: {toplam_binis}") 
        
                    

        except FileNotFoundError:  
                print("Biniş verisi dosyası bulunamadı.") 
   
       



