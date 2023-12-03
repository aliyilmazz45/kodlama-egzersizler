baslangic= int(input("baslangıç değerini girin:"))
bitis = int(input("bitiş değerini girin"))
liste = [x for x in range(baslangic,bitis+1) if x%2==0]
print(liste)