sayi=int(input("kontrol etmek istediginiz sayiyi girin:"))
sayi_liste = list(str(sayi))

n = len(sayi_liste)
total = 0
for i in sayi_liste:
    total += int(i) ** n

if total == sayi:
    print(f"{sayi} sayısı bir armstrong sayısıdır.")
else:
    print(f"{sayi} sayısı bir armstrong sayısı degildir.")
