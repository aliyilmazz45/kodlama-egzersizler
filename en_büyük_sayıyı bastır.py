sayi1 = float(input("1. sayinizi girin:"))
sayi2 = float(input("2.sayinizi girin:"))
sayi3 = float(input("3.sayinizi girin:"))
if sayi1>sayi2:
    if sayi1>sayi3:
        print(f"en büyük sayi :{sayi1}")
    elif sayi3>sayi1 :
        print(f"en büyük sayi:{sayi3}")
elif sayi2>sayi1:
    if sayi2>sayi3:
        print(f"en büyük sayi:{sayi2}")
    elif sayi3>sayi2:
        print(f"en büyük sayi:{sayi3}")
