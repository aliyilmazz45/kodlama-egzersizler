def tam_bolen(sayi):
    liste = []
    for i in range(1,sayi+1):
        if sayi%i==0:
            liste.append(i)
    print (liste)

while True:
    sayi=input("bölenlerini göremk istediginiz sayıyı girin ya da çıkış yapmak için 'q' ya basın: ")
    if sayi=="q":
        print("çıkış yapıldı")
        break
    else:
        sayi=int(sayi)
        tam_bolen(sayi)



