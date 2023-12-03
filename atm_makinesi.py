
bakiye =1000
sifre=12345
giris_hakki=3

print("****** ATM MAKİNESİNE HOŞGELDİNİZ ******")
while True:
    sifre1=int(input("sifrenizi girin:"))
    if sifre !=sifre1:
        print("hatalı şifre girdiniz.")
        giris_hakki-=1
    if giris_hakki==0:
        print("çok fazla hatalı giriş yaptınız.")
        break
    elif sifre1==sifre:
        print("giriş başarılı.")

        print("*****İŞLEM SEÇİNİZ****\n"
              "1-BAKİYE SORGULAMA\n"
              "2-PARA YATIRMA\n"
              "3-PARA ÇEKME\n"
              "ÇIKIŞ İÇİN 4 YA BASIN")
        while True:
            islem=int(input("yapmak istediginiz işlemi girin(1/2/3/4):"))
            if islem==1:
                print("bakiye sorgulama işlemini seçtiniz.")
                print(f"bakiyeniz {bakiye} TL dir")
            elif islem ==2:
                print("para yatırma işlemini seçtiniz.")
                bakiye2=int(input("yatırmak istediginiz miktarı girin:"))
                bakiye = bakiye+bakiye2
                print(f"güncel bakiyeniz {bakiye} TL dir. ")
            elif islem==3:
                print("para çekme işlemini seçtiniz.")
                bakiye3=int(input("çekmek istediginiz miktarı girin:"))
                if bakiye3> bakiye:
                    print("yetersiz bakiye.")
                elif bakiye>=bakiye3:
                    bakiye=bakiye-bakiye3
                    print(f"güncel bakiyeniz {bakiye} TL dir.")
            elif islem==4:
                print("çıkış yapılmıştır.")
                break
            else:
                print("hatalı tuşlama yaptınız.")

        break




