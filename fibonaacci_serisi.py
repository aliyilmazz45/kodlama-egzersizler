a = 1
b = 1

sayi=int(input("kaçıncı basamağa kadar fibonacci yazmak istersiniz:"))
print(1)
print(1)
for i in range(sayi-2):
    a , b = b , a+b
    print(a+b)
