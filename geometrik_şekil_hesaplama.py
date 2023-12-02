print("*** GEOMETRİK ŞEKİL HEAPLAMA ***")
sekil = input("heaplamak istediginiz şekli yazın(üçgen/dörtgen):")
if sekil == "ücgen":
    kenar1 = int(input("ilk kenar uzunlugunu girin:"))
    kenar2 = int(input("ikinci kenar uzunlugunu girin:"))
    kenar3 = int(input("ücüncü kenar uzunlugunu girin:"))
    if not( abs(kenar1+kenar2)>kenar3 and kenar3>abs(kenar1-kenar2) and abs(kenar1+kenar3)>kenar2 and kenar2>abs(kenar1-kenar3) and abs(kenar2+kenar3)>kenar1 and kenar1>abs(kenar2-kenar3)):
        print("girdiginiz kenarlarla ücgen belirtmiyor!!!")
    elif  kenar1==kenar2 and kenar2== kenar3:
        print("girdiginiz kenarlar eskenar ücgene aittir.")
    elif kenar1==kenar2 or kenar2==kenar3 or kenar1==kenar3:
        print("girdiginiz kenarlar ikizkenar ücgene aittir.")
    else:
        print("girdiginiz kenarlar cesitkenar ücgene aittir.")

elif sekil== "dörtgen":
    kenar11 = int(input("ilk kenar uzunlugunu girin:"))
    kenar12 = int(input("ikinci kenar uzunlugunu girin:"))
    kenar13 = int(input("ücüncü kenar uzunlugunu girin:"))
    kenar14 = int(input("dördüncü kenar uzunlugunu girin:"))
    if kenar11==kenar12 and kenar12==kenar13 and kenar13==kenar14:
        print("girdiginiz kenarlar kareye aittir.")
    elif (kenar11==kenar13 and kenar12== kenar14 and kenar12!=kenar13) :
        print("girdiginiz kenarlar dikdötrgene aittir.")
    else:
        print("girdiginiz kenarlar özel olmayan bir dörtgene aittir.")
else:
    print("lütfen verilen seçeneklerden birini giriniz.")
