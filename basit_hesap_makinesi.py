sayi1 = float(input("1.sayinizi girin:"))
islem = input("islem giriniz:")
sayi2 = float(input("2.sayinizi girin:"))
if islem == "+":
    print(f"islemin sonucu : {sayi1+sayi2}")
elif islem == "-":
    print(f"islemin sonuucu: {sayi1 - sayi2}")
elif islem == "*":
    print(f"islemin sonucu: {sayi1 * sayi2}")
elif islem == "/":
    print(f"islemin sonucu : {sayi1 / sayi2}")
else:
    print("geçersiz islem girdiniz!!!")
