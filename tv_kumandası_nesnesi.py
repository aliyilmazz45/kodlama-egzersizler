class kumanda():

    def __init__(self, durum="kapalı", ses=0, liste = [ "trt","show","fox","star","atv","kanal d" ] , kanal="trt"):
        self.durum = durum
        self.ses = ses
        self.liste = liste
        self.kanal_indeks = 0
        self.kanal = kanal



    def acma(self):

        if self.durum == "açık":
            print("tv zaten açık.")

        else:
            self.durum = ("açık")
            print("tv açıldı")



    def kapama(self):

        if self.durum == "kapalı":
            print("tv zaten kapalı")

        else:
            self.durum = "kapalı"
            print("tv kapatılıd.")



    def ses_durum(self):

        while True:

            islem = input("ses arttırmak için + azaltmak için -  çıkış için * tusuna basın.")

            if islem == "+":

                if self.ses != 32:
                    self.ses += 1
                    print(self.ses)


            elif islem == "-":

                if self.ses != 0:
                    self.ses -= 1
                    print(self.ses)

            elif islem == "*":
                print("ses ayarlarından çıkış yapılıyor...")
                break

            else:
                print("hatalı tuşlama yaptınız.")



    def kanal_ekle(self, a):
        self.liste.append(a)
        print(f"güncel kanal listeniz:{self.liste}")



    def kanal_sil(self, b):
        self.liste.remove(b)
        print(f"güncel kanal listeniz:{self.liste}")



    def kanal_degis(self):

        while True:

            islem = input("üst kanala geçmek için + alt kanala geçmek için - kanal seçiminden çıkmak için * ya basın.")


            if islem == "+":

                if len(self.liste) - 1 == self.kanal_indeks:
                    self.kanal_indeks = 0

                else:
                    self.kanal_indeks += 1
                self.kanal = self.liste[self.kanal_indeks]
                print("mevcut kanal", self.kanal)

            elif islem == "-":

                if self.kanal_indeks == 0:
                    self.kanal_indeks = len(self.liste) - 1


                else:
                    self.kanal_indeks -= 1
                self.kanal = self.liste[self.kanal_indeks]
                print("mevcut kanal", self.kanal)



            elif islem == "*":
                break


            else:
                print("hatalı tuşlama yaptınız")


    def bilgi(self):
        print(f"""  
        tv durumu {self.durum}
        tv ses {self.ses}
        tv kanal listesi {self.liste}
        tv kanal {self.kanal}


        """)


kumanda = kumanda()
print(""""
*** KUMANDA PROGRAMI ***
 İŞLEMLER 
 1- tv açma 
 2- tv kapama
 3- ses değştirme
 4- kanal değiştirme
 5- kanal listesini aç
 6- kanal ekle
 7- kanal sil
 8- tv bilgi
 9-kanal sayısını öğrenme
 0- çıkış


""")

while True:

    islem = int(input("yapmak istediginiz işlemin kodunu tuşayın:"))

    if islem == 0:
        print("kumandadan çıkış yapılıyor")
        break

    elif islem == 1:
        kumanda.acma()

    elif islem == 2:
        kumanda.kapama()

    elif islem == 3:
        kumanda.ses_durum()

    elif islem == 4:
        kumanda.kanal_degis()

    elif islem == 5:
        print(f"listeniz:{kumanda.liste}")

    elif islem == 6:
        y = input("eklemek istediginiz kanalı girin.")
        kumanda.kanal_ekle(y)

    elif islem == 7:
        x = input("silmek istediğiniz kanlaı girin:")
        kumanda.kanal_sil(x)

    elif islem == 8:
        kumanda.bilgi()

    elif islem == 9:
        print("tv de olan kanal sayısı:", len(kumanda.liste))

    else:
        print("hatalı tuşlama yaptınız.")









