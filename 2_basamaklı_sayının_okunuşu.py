birler =[" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar =["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
def okunus(sayi):
    birinci=sayi%10
    ikinci = sayi//10
    return onlar[ikinci]+" "+birler[birinci]
sayi=int(input("okunuşunu yazdırmak istediginiz sayiyi girin:"))
print(f"{sayi} sayısının okunuşu {okunus(sayi)} şeklindedir.")