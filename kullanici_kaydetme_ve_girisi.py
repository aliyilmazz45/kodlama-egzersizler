print("*****KULLANICI KAYDETME*****")
sys_kullanici_adi =input("kaydetmek istediginiz hesabın kullanici adini seciniz:")
sys_sifre = int(input("kaydetmek istediginiz hesabın sifresini seciniz:"))
print("*****KULLANİCİ GİRİSİ*****")
kullanici_adi = input("kullanici adinizi girin:")
sifre = int(input("sifrenizi girin:"))
if kullanici_adi == sys_kullanici_adi and sifre == sys_sifre:
    print("giris basarili")
else:
    print("kullanici adi ya da sifre hatalı!!!")
