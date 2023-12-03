toplam=0
while True:
    sayi=input("toplamak istediğiniz sayiyi girin(çıkış yapıp sonucu göremk için 'q' ya basın):")
    if sayi=="q":
        print("işlem bitirilmiştir.")
        break
    sayi=int(sayi)
    toplam+=sayi
print(f"girdiğiniz sayıların toplamı {toplam} sayısına eşittir.")