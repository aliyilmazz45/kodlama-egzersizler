def mukemmel_sayi(sayi):
    i=1
    toplam=0
    while i<sayi:
        if sayi%i==0:
            toplam+=i
        i+=1
    if sayi==toplam:
        return True
baslangic=int(input("başlangıç değerini girin:"))
bitis=int(input("bitiş deperini girin:"))
liste = []
while baslangic<bitis+1:
    if mukemmel_sayi(baslangic):
        liste.append(baslangic)
    baslangic+=1
print(liste)