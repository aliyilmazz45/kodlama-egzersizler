import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Hata: Sıfıra bölme hatası"

def us_alma(x, y):
    return math.pow(x, y)

def karekok_alma(x):
    return math.sqrt(x)

while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Alma")
    print("0. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (0-6): ")

    if secim == "0":
        print("Hesap makinesi kapatılıyor...")
        break
    elif secim in ["1", "2", "3", "4", "5", "6"]:
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            if secim != "6":
                sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Hata: Geçersiz sayı girişi")
            continue

        if secim == "1":
            sonuc = toplama(sayi1, sayi2)
        elif secim == "2":
            sonuc = cikarma(sayi1, sayi2)
        elif secim == "3":
            sonuc = carpma(sayi1, sayi2)
        elif secim == "4":
            sonuc = bolme(sayi1, sayi2)
        elif secim == "5":
            sonuc = us_alma(sayi1, sayi2)
        elif secim == "6":
            sonuc = karekok_alma(sayi1)

        print("Sonuç: ", sonuc)
    else:
        print("Hata: Geçersiz seçim")
