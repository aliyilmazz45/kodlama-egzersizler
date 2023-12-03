print("*** KULLANICI KAYDETME ***")
username =input("kaydetmek istediginiz hesabın kullanıcı adınızı seçin:")
password = int(input("kaydetmek istediginiz hesabın şifresini seçin:"))
giris_hakki =3
print("*** KULLANICI GİRİŞİ ***")
while True:
    username1=input("giriş için kullanıcı adınızı girin:")
    password1 =int(input("giriş için şifrenizi"))
    if username!=username1 or password != password1:
        print("Hatalı kullanıcı adı ya da şifre girdiniz!!!")
        giris_hakki-=1
    if giris_hakki==0:
        print("deneme hakkınız bitti.")
        break

    elif username==username1 and password == password1 :
        print("giriş başarılı.")
        break

