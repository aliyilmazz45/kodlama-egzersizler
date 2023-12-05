import random
import time
print("*****************************")
print("TAHMİN OYUNUNA HOŞGELDİNİZ")
print("*****************************")
sayi = random.randint(1, 100)
tahmin_hakki = 7
while True:
    tahmin = int(input("tahminizi girin(1-100):"))
    if tahmin>sayi:
        print("tahmininiz kontrol ediliyor...")
        time.sleep(1)
        print("daha küçük bir sayı tahmin edin")
        tahmin_hakki-=1
    elif tahmin<sayi:
        print("tahminiz kontrol ediliyor...")
        time.sleep(1)
        print("daha büyük bir sayı tahmin edin.")
        tahmin_hakki-=1
    else:
        print("tahminiz kontrol ediliyor...")
        time.sleep(1)
        print("tebrikler doğru tahmin ettiniz.")
        break
    if tahmin_hakki==0:
        print("tahmin hakkınız doldu")
        print(f"tuttugum sayı {sayi} sayısıydı.")

