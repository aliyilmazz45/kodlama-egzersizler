print("*****KULLANICI GİRİSİ*****")
sys_kullanici_adi ="aliyilmazz._"
sys_sifre = 123456
kullanici_adi = input("kullanici adinizi girin:")
sifre = int(input("sifrenizi girin:"))
if kullanici_adi==sys_kullanici_adi and sifre == sys_sifre:
    print("giris basarili")
else:
    print("kullanici adi yad sifre hatalı!!!")
