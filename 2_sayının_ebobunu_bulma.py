def ebob(a,b):
    ebob=1
    i=1
    while (i<=a and i<=b):
        if a%i==0 and b%i==0:
            ebob=i
        i+=1
    return ebob
sayi1=int(input("ilk sayiyi girin:"))
sayi2=int(input("ikinci sayiyi girin:"))
ebob(sayi1,sayi2)
print(f"{sayi1} ve {sayi2} sayılarının ebobu {ebob(sayi1,sayi2)} sayısıdır.")