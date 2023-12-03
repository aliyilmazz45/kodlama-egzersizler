sayi= int(input("kontrol etmek istediginiz sayiyi girin:"))
i=1
toplam=0
while i < sayi:
    if sayi % i==0:
        toplam += i
    i+=1
if toplam==sayi:
    print(f"{sayi} mükkemmel sayıdır.")
else:
    print(f"{sayi} mükemmel sayi değildir.")