def asal_mi():
    sayac=0
    i=1
    sayi=int(input("kontrol etmek istediginiz sayıyı girin:"))
    if sayi==1:
        print("1 sayısı asal sayı değildir")
    else:
        while i<sayi+1:
            if sayi%i==0:
                sayac+=1
            i+=1
        if sayac==2:
            print(f"{sayi} sayısı asal sayıdır.")
        else:
            print(f"{sayi} sayısı asal sayı değildir.")

asal_mi()




