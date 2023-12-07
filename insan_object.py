class insan():
    def __init__(self, isim="bilgi yok", soyisim="bilgi yok", meslek="bilgi yok", sirket="bilgi yok",
                 medeni_durum="bilgi yok", maas=0, ):
        self.isim = isim
        self.soyisim = soyisim
        self.meslek = meslek
        self.sirket = sirket
        self.medeni_durum = medeni_durum
        self.maas = maas

    def bilgi(self):
        print(f"""   
    isim:{self.isim}
    soyisim:{self.soyisim}
    meslek:{self.meslek}
    sirket:{self.sirket}
    medeni_durum:{self.medeni_durum}
    maas:{self.maas}""")

    def sirket_degis(self, sirket):
        print("sirket degiştirildi")
        self.sirket = sirket

    def evlilik(self, ):
        print("medeni durum değiştirildi.")
        self.medeni_durum = "evli"

    def bosanma(self, ):
        print("medeni durum degistiriliyor")
        self.medeni_durum = "bekar"

    def zam_yap(self, zam_miktari):
        print(zam_miktari, "TL zam yapıldı.")
        self.maas += zam_miktari
