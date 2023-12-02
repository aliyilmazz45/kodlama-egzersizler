boy = float(input("boyunuzu cm cinsinden girin:"))
kilo = float(input("kilonuzu kg cinsinden giriniz:"))
boym = boy/100
boy_kilo_endeksi = kilo/(boym*boym)
if boy_kilo_endeksi<18.5:
    print("zayıfsın az kilo al")
elif 18.5<boy_kilo_endeksi and boy_kilo_endeksi<25:
    print("normal kilodasın helal")
elif 25 < boy_kilo_endeksi and boy_kilo_endeksi < 30:
    print("fazla kilolusun az kilo ver!!!")
elif   30 < boy_kilo_endeksi :
    print("obez olmuşsun :(((")


